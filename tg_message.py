import tg_keyboard, config


def send_message(bot, bot_name, bot_action, info, chat_id):
    print('send_message', bot_name, bot_action, info, chat_id)
    if 'bot-info' in bot_action:
        for item in info['position']:
            message_text = config.text_message[bot_action] % ('🟥' if float(item['positionAmt']) < 0 else '🟩', item['symbol'], round(float(item['unrealizedProfit']), 2), '©' if not item['isolated'] else '', item['leverage'], round(float(item['positionAmt']), 2), round(float(item['entryPrice']), 4), round(float(item['notional']), 2), round(float(item['initialMargin']), 2))

            data = {}
            data['position'] = item['symbol']
            data['side'] = 'SELL' if float(item['positionAmt']) < 0 else 'BUY'
            data['order'] = []

            for i in item['order']:
                data['order'].append(i)

                message_text += config.text_message['drop-line']
                message_text += config.text_message['order'] % (i['type'], i['side'], i['stopPrice'])

            print('data', data)

            inline_keyboard = tg_keyboard.inline_keyboard(bot_name, bot_action, data)
            bot.send_message(chat_id, message_text, reply_markup=inline_keyboard, parse_mode='HTML')

        message_text = config.text_message['balance'] % (round(float(info['balance']['totalMarginBalance']), 2), round(float(info['balance']['totalUnrealizedProfit']), 2), round(float(info['balance']['totalWalletBalance']), 2))
        print('message_text', message_text)

    elif 'manual_close' in bot_action:
        print('оповещение о закрытии')
        print(info['new_position']['code'])
        if info['new_position']['code'] == '00':
            message_text = config.text_message['close_position'] % ('ручное закрытие', info['open_position']['symbol'], 'BUY' if float(info['open_position']['positionAmt']) > 0 else 'SELL',
                    info['open_position']['positionAmt'], info['open_position']['symbol'], info['open_position']['unRealizedProfit'], info['open_position']['entryPrice'])
            print(message_text)
        else:
            print('оповещение об ошибке')
            message_text = config.text_message['error'] % (info['new_position']['message']['code'], info['new_position']['message']['message'])
            print(message_text)

        message_text += config.text_message['drop-line']

        if info['orders']['code'] == '00':
            message_text += config.text_message['close_all_orders']
            print(message_text)

        else:
            message_text += config.text_message['error'] % (info['orders']['message']['code'], info['orders']['message']['msg'])
            print(message_text)

    elif 'close_order' in bot_action:
        print('оповещение о закрытии')
        if info['orders']['code'] == '00':
            message_text = config.text_message['close_order'] % (info['orders']['message']['origType'], info['orders']['message']['symbol'], info['orders']['message']['stopPrice'])

        else:
            message_text = config.text_message['error'] % (info['orders']['message']['code'], info['orders']['message']['msg'])

    markup = tg_keyboard.keyboard("main")
    send_request = bot.send_message(chat_id, message_text, reply_markup=markup, parse_mode='HTML')

    return {
            'code': '00',
            'message': send_request
        }