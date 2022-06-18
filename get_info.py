import config, logging

from binance.client import Client
from binance.enums import *

logging.basicConfig(level=logging.DEBUG)


def account_info(bot_name):
    data = {}

    if config.binance_settings['TESTNET']:
        client = Client(config.binance_settings['API_KEY_TEST'], config.binance_settings['API_SECRET_TEST'],
                        testnet=True)
    else:
        client = Client(config.binance_settings[bot_name]['API_KEY'], config.binance_settings[bot_name]['API_SECRET'])

    account_info = client.futures_account()
    orders_info = client.futures_get_open_orders()
    print('orders_info', orders_info)

    data['balance'] = {'totalWalletBalance': account_info['totalWalletBalance'], 'totalUnrealizedProfit': account_info['totalUnrealizedProfit'], 'totalMarginBalance': account_info['totalMarginBalance']}

    position = []
    [position.append(item) for item in account_info['positions'] if float(item['initialMargin']) != 0]

    for i in position:
        i['order'] = []
        for item in orders_info:
            if i['symbol'] == item['symbol']:
                i['order'].append(item)

    data['position'] = position

    print('position', position)
    print('data', data)

    return data