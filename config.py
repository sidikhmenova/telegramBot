telegram_settings = {
    'local_work': True,
    'WEBHOOK_URL_BASE_real': 'https://katietalipova.pythonanywhere.com',
    'WEBHOOK_URL_BASE_local': 'https://d32e-92-37-239-241.ngrok.io',
    'telegram_token_real': '5087818121:AAGeMApjqaXDF2kzOa6TU3Bc2X_I1KXtPZ8',
    'telegram_token_local': '424687958:AAF93BeRZyoBCUb6UMugqDGviZz02Va2x0g',
    'telegram_users_real': ['399865944', '1094561715'],
    'telegram_users_local': ['399865944', '1094561715']
}

binance_settings = {
    'TESTNET': True,
    'kate': {
        'API_KEY': 'qvDT51wkb5RaurIvgIrPQ4TjmMar8ZRLlOCtkgheTYaFYw5lJxRBkutUZZo6seE1',
        'API_SECRET': '4749q5vRnzlRQbfFThCIOnC15El4dWO9nOPrd8uVjh1zrKnekuRlAQWpOamqcpxe',
    },
    'ant': {
        'API_KEY_ant': 'wCNIJIVTYftvFrEqqOj0lPYXAGwUKyd7s1DJ2qG7Xb1QLZkYqTs16E0A6Hd3o2KA',
        'API_SECRET_ant': 'sGx0NjMT2QlhoHWSCIrC5IQuxwIQfhMwOK9kBKWFgKaTFdYnMXIGtGlctGQwfWWQ',
    },
    'API_KEY_TEST': 'd4b677593e6d92620e02134a0ab2c20efc392bfac95d35741c93c816414d2868',
    'API_SECRET_TEST': '04071d34b8a694db1bd909d7048e02dba0e9030c5689321a5e5f59a7d7d654fb'
}

text_message = {
    'bot-info': '%s<b>%s</b> PNL: <b>%s</b> %s<b>x%s</b>\nкол-во: %s, entry price: %s\nсумма: %s USDT, маржа: %s USDT\n',
    'drop-line': '----------------\n',
    'order': '<b>%s</b> %s -- %s\n',
    'balance': '💵 Баланс (общий): <b>%s</b> \nPNL: %s \nКошелек: %s ',
    'error': '⚠ Внимание, где-то ошибка\n код: <b>%s</b> %s!',
    'close_position': '❌ <b>%s</b> - close <b>%s</b>\n%s %s %s, PNL: <b>%s</b> \nentry price: %s \n',
    'close_order': '✖ Ордер <b>%s</b> по <b>%s</b> на цену %s отменен',
    'close_all_orders': '✖ Все ордера закрыты',
    'alert': '📢 <b>%s</b> (%s) -- <b>%s</b> -- count: <b>%s</b> -- price: <b>%s</b>\n <u>%s</u> \n',
    'enter_position': '☑ <b>%s</b> -- %s <b>%s</b> total:<b>%s</b>, price: %s, count: %s \n',
    'stop_order':  '⛔ SL: price: <b>%s</b> \n',
    'trailing_order':  '❎ TS: act.price: <b>%s</b> -- r: <b>%s</b>',
    'no order': '❌ Бот выключен для покупок',
    'работает ➡ выключить': 'меняю статус на ВЫКЛЮЧЕН',
    'не работает ➡ включить': 'меняю статус на ВКЛЮЧЕН',
    'change_status': 'меняю статус',
    'orders': '▫ <b>%s</b> PNL: <b>%s</b>\nкол-во: %s (сумма входа %s USDT, маржа %s USDT), entry price: %s\n',
    'new_open_position': '✅ <b>%s - enter %s</b>\n%s %s %s',
    'new_open_position_error': '⚠ Внимание, где-то ошибка\n%s\n<b>close</b> %s\n%s %s',
    'new_close_position_error': '⚠ Внимание, где-то ошибка\n%s\n<b>close</b> %s\n%s %s entry_price: %s\n📢 <b>%s</b> (%s) -- <b>%s</b> -- count: <b>%s</b> -- price: <b>%s</b>\n <u>%s</u> \n',
    'new_close_position_error_withoutalert': '⚠ Внимание, где-то ошибка\n%s\n<b>close</b> %s\n%s %s entry_price: %s\n',
    'new_close_position_empty': '❌ <b>%s - close</b> Нечего закрывать \n📢 <b>%s</b> (%s) -- <b>%s</b> -- count: <b>%s</b> -- price: <b>%s</b>\n <u>%s</u> \n',
    'no_orders': '➖ Нет открытых позиций',
    'no_command': '🤷‍♀️Прости, я не умею это делать',
    'scalping_settings': '⚙ ️Текущие настройки:\nпара: <b>%s</b>\n⤒ %s , ⤓ %s\n⤒ %s , ⤓ %s\nтрейлинг: %s',
    'scalping_settings_result': '✅ Поздравляю, изменил значения на:',
    'scalping_settings-help': '<b>Для изменения настроек введите:</b>\n<b>/edit @пара</b> @ ⤒% @ ⤓% @ ⤒side @ ⤓side @ трейлинг\n\nПример: <i>/edit @ unfiusdt @ 0.4 @ -0.4 @ SELL @ BUY @ 0.2</i>'
}

inline_buttons = {
    'bot-info': 'manual_close',
    'close_order': 'close_order'
}

inline_buttons_text = {
    'manual_close': '❌ Закрыть позицию %s',
    'close_order': '✖ %s %s'
}

keyboard_buttons = ['работает ➡ выключить', 'не работает ➡ включить', '💵 Kate bot-info', '💵 Ant bot-info', '⚙ Настроить скальпинг-бота']

error_list_block = []

error_list_ok = [200]

error_list_repeat = [-1000, -1001, -1002, -1003, -1004, -1005, -1006, -1007, -1010, -1011, -1013, -1015, -1021, -2020, -4015, -4082, -4083, -4084, -4088, -4140, -4165]

error_list_change = [-2021]
