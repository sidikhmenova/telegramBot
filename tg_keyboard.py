import telebot, config, main

from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


def keyboard(key_type="main"):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    print('keyboard')
    print(main.bot_status)

    if key_type == "main":

        row = [KeyboardButton(x) for x in config.keyboard_buttons[:1] if main.bot_status == 'work']
        markup.add(*row)
        row = [KeyboardButton(x) for x in config.keyboard_buttons[:2] if main.bot_status == 'unwork']
        markup.add(*row)
        row = [KeyboardButton(x) for x in config.keyboard_buttons[2:4]]
        markup.add(*row)
        row = [KeyboardButton(x) for x in config.keyboard_buttons[6:7]]
        markup.add(*row)

    return markup


def inline_keyboard(bot_name, bot_action, data):
    print('inline_keyboard', bot_name, bot_action, data)
    markup = InlineKeyboardMarkup()
    markup.row_width = 2

    if bot_action == 'bot-info':

        callback = config.inline_buttons[bot_action] + '@' + bot_name + '@' + data['position'] + '@' + data['side']
        print('callback', callback)

        text = config.inline_buttons_text[callback.split('@')[0]] % (data['position'])
        print('inline text', text)
        markup.add(InlineKeyboardButton(text=text, callback_data=callback))

        array_inline = []
        for i in data['order']:
            callback = config.inline_buttons['close_order'] + '@' + bot_name + '@' + str(i['symbol']) + '@' + str(i['orderId'])
            print('callback', callback)

            text = config.inline_buttons_text[callback.split('@')[0]] % (i['type'], i['side'])
            print('inline text', text)

            array_inline.append({'callback': callback, 'text': text})

        row = [InlineKeyboardButton(text=x['text'], callback_data=x['callback']) for x in array_inline]
        print('row', row)
        markup.add(*row)

    return markup