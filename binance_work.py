import config, logging, json, asyncio, time

from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException
from colorama import init, Fore
from colorama import Back
from colorama import Style

logging.basicConfig(level=logging.DEBUG)


def new_request(bot_name, bot_action, symbol, id):
    print('new_request', bot_name, bot_action, symbol, id)
    if config.binance_settings['TESTNET']:
        print('2')
        client = Client(config.binance_settings['API_KEY_TEST'], config.binance_settings['API_SECRET_TEST'],
                        testnet=True)
    else:
        client = Client(config.binance_settings[bot_name]['API_KEY'], config.binance_settings[bot_name]['API_SECRET'])

    if bot_action == 'manual_close':
        print('2')
        request_close = close_open_position(client, symbol, id)

    elif bot_action == 'close_order':
        request_close = cancel_open_orders(client, symbol, id)

    else:
        request_close = {}
        request_close['code'] = '05'
        request_close['message'] = 'unknown message'

    return request_close


def close_open_position(client, symbol, position_side):
    print('2')

    symbol_position = client.futures_position_information(symbol=symbol)
    print('symbol_position', symbol_position)
    symbol_position = {'open_position': symbol_position[0]}
    # request_result['open_position'] = symbol_position[0]

    if float(symbol_position['open_position']['positionAmt']) > 0 and position_side == 'BUY' or float(symbol_position['open_position']['positionAmt']) < 0 and position_side == 'SELL':
        print('ljitk')
        request_close_position = send_order(
            client=client,
            type_order='MARKET',
            symbol=symbol,
            side='SELL' if position_side == 'BUY' else 'BUY',
            quantity=abs(float(symbol_position['open_position']['positionAmt']))
        )

        print('request_position', request_close_position)

        if request_close_position['new_position']['code'] == '00':
            request_cancel_orders = cancel_open_orders(client, symbol)
            print('request_cancel_orders', request_cancel_orders)
        else:
            request_cancel_orders = []

        print('result request_position', symbol_position | request_close_position | request_cancel_orders)

        return symbol_position | request_close_position | request_cancel_orders


def cancel_open_orders(client, symbol, order_id=None):
    print('cancel_open_orders', client, symbol, order_id)
    print(type(order_id))
    try:
        if order_id is not None:
            cancel_order = client.futures_cancel_order(
                symbol=symbol,
                orderId=order_id,
                recvWindow='60000')
            print('cancel_order', cancel_order, flush=True)

        else:
            cancel_order = client.futures_cancel_all_open_orders(
                symbol=symbol,
                recvWindow='60000')
            print('cancel_order', cancel_order, flush=True)

        result = check_request_result(cancel_order)
        print('result', result)

        if result['code'] == '01':
            cancel_open_orders(client, symbol, order_id)

        print('result cancel_open_orders', result)
        return {'orders': result}

    except BinanceAPIException as e:
        request = {}
        request['code'] = e.status_code
        request['message'] = e.message

        return {'orders': check_request_result(request)}


def send_order(client, type_order, symbol, side, quantity):
    print('send_order', client, type_order, symbol, side, quantity)
    try:
        send_order = client.futures_create_order(
            type=type_order,
            symbol=symbol,
            side=side,
            quantity=quantity
        )

        result = check_request_result(send_order)
        print('close_position', send_order)
        print('close_position', result)

        if result['code'] == '01':
            send_order(client, type_order, symbol, side, quantity)

        print('result send_order', result)

        return {'new_position': result}

    except BinanceAPIException as e:
        request= {}
        request['code'] = e.status_code
        request['message'] = e.message

        return {'new_position': check_request_result(request)}


def check_request_result(request):
    # 1) если все успешно (не вернулся тег code)
    if 'code' not in request:
        print(Fore.MAGENTA + 'ордер отправлен')
        return {
            'code': '00',
            'message': request
        }

    # если вернулся код, но код считается успешным
    elif 'code' in request and request['code'] in config.error_list_ok:
        print(Fore.MAGENTA + 'ордер отправлен')
        return {
            'code': '00',
            'message': request
        }

    # 3) произошла ошибка и нужно повторить ордер
    elif 'code' in request and request['code'] in config.error_list_repeat:
        print(Fore.RED + '3) произошла ошибка и нужно повторить ордер', flush=True)

        return {
            'code': '01',
            'message': request
        }

    # 4) произошла ошибка и ничего не поделаешь
    else:
        print(Fore.RED + '4) произошла ошибка и ничего не поделаешь', request, flush=True)
        return {
            'code': '02',
            'message': request
        }