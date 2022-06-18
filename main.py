import logging, telebot, config, time, flask, tg_keyboard, get_info, tg_message, binance_work

from telebot import custom_filters
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask, request, render_template

import binance_work

app = Flask(__name__)

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

if config.telegram_settings['local_work']:

    WEBHOOK_URL_BASE = config.telegram_settings['WEBHOOK_URL_BASE_local']
    bot = telebot.TeleBot(config.telegram_settings['telegram_token_local'])
    WEBHOOK_URL_PATH = "/%s/" % (config.telegram_settings['telegram_token_local'])

else:
    WEBHOOK_URL_BASE = config.telegram_settings['WEBHOOK_URL_BASE_real']
    bot = telebot.TeleBot(config.telegram_settings['telegram_token_real'])
    WEBHOOK_URL_PATH = "/%s/" % (config.telegram_settings['telegram_token_real'])

bot_status = 'work'

bot.delete_my_commands(scope=None, language_code=None)
bot.set_my_commands(
    commands=[
        telebot.types.BotCommand("kate_balance", "Kate баланс бота"),
        telebot.types.BotCommand("kate_orders", "Kate список сделок"),
    ],

)

cmd = bot.get_my_commands(scope=None, language_code=None)

# Empty webserver index, return nothing, just http 200
@app.route('/', methods=['GET', 'HEAD'])
def index():
    return ''


# Process webhook calls
@app.route(WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)

@bot.message_handler(chat_id=[399865944], commands=['kate_balance'])
def send_welcome(message):
    print('получил')

    return 'ok'

@bot.message_handler(chat_id=[399865944], commands=['kate_orders'])
def send_welcome(message):
    print('получил')

    return 'ok'


# Handle all other messages
@bot.message_handler(chat_id=[399865944], func=lambda message: True, content_types=['text'])
def echo_message(message):
    print(message.text)

    if 'работает ➡ выключить' in message.text:
        bot_status = 'unwork'

    elif 'не работает ➡ включить' in message.text:
        bot_status = 'work'

    elif 'bot-info' in message.text:
        bot_name = message.text.split(' ')[1]
        bot_action = message.text.split(' ')[2]

        info = get_info.account_info(bot_name)
        tg_message.send_message(bot, bot_name, bot_action, info, message.chat.id)
        print(info)

    elif 'Настроить' in message.text:
        print('1')


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    request = binance_work.new_request(
        bot_name=call.data.split('@')[1],
        bot_action=call.data.split('@')[0],
        symbol=call.data.split('@')[2],
        id=call.data.split('@')[3]
    )
    print('request', request)

    send_message = tg_message.send_message(
        bot=bot,
        bot_name=call.data.split('@')[1],
        bot_action=call.data.split('@')[0],
        info=request,
        chat_id=call.from_user.id
    )

    bot.edit_message_reply_markup(
        chat_id=call.from_user.id,
        message_id=call.message.id,
        reply_markup=None
    )


    # if call.data.split('@')[0] == "manual_close":
    #     print('отправляю на закрытие', call)

    #     request = binance_work.new_request(
    #         bot_name=call.data.split('@')[1],
    #         bot_action=call.data.split('@')[0],
    #         symbol=call.data.split('@')[2],
    #         id=call.data.split('@')[3]
    #     )
    #     print('request', request)
    #
    #     send_message = tg_message.send_message(
    #         bot=bot,
    #         bot_name=call.data.split('@')[1],
    #         bot_action=call.data.split('@')[0],
    #         info=request,
    #         chat_id=call.from_user.id
    #     )
    #
    #     if request['new_position']['code'] == '00':
    #         bot.edit_message_reply_markup(
    #             chat_id=call.from_user.id,
    #             message_id=call.message.id,
    #             reply_markup=None
    #         )
    #
    # elif call.data.split('@')[0] == "close_order":
    #     print('отправляю на закрытие ордера')
    #
    #     request = binance_work.new_request(
    #         bot_name=call.data.split('@')[1],
    #         bot_action=call.data.split('@')[0],
    #         symbol=call.data.split('@')[2],
    #         id=call.data.split('@')[3]
    #     )
    #
    #     send_message = tg_message.send_message(
    #         bot=bot,
    #         bot_name=call.data.split('@')[1],
    #         bot_action=call.data.split('@')[0],
    #         info=request,
    #         chat_id=call.from_user.id
    #     )
    #
    #     bot.edit_message_reply_markup(
    #         chat_id=call.from_user.id,
    #         message_id=call.message.id,
    #         reply_markup=None
    #     )
    #
    #
    #
    #     print('request', request)


bot.add_custom_filter(custom_filters.ChatFilter())


bot.remove_webhook()
time.sleep(1)
bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
