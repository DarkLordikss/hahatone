from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, CallbackContext

print("Bot is working!")

users = {
    1233164455: {
        "balance": 100,
        "tokens": {}
    }
}
market = {
    '123': {
        "user_id": 1233164455,
        "price": 10,
        "url": 'http://techslides.com/demos/sample-videos/small.mp4'
    }
}


def start(update, context):
    if not users.get(update.effective_user.id):
        users[update.effective_user.id] = {
            "balance": 100,
            "tokens": {}
        }
    message = "Привет, я Оки Токен~ Напиши /help, чтобы узнать больше."
    update.message.reply_text(message)


def help_command(update, context):
    message = "Доступные команды:\n"
    message += "/start - Приветствие\n"
    message += "/buy - Купить NFT\n"
    message += "/sell - Продать NFT\n"
    message += "/info - Информация о боте\n"
    message += "/balance - Баланс\n"
    message += "/tokens - Твои токены\n"
    update.message.reply_text(message)


def tockens_command(update, context):
    print(users)
    print(users[update.effective_user.id])
    if users[update.effective_user.id]['tokens'] != {}:
        message = 'Вот твои токены~\n\n'
        update.message.reply_text(message)
        for token in users[update.effective_user.id]['tokens']:
            context.bot.send_video(update.message.chat.id, users[update.effective_user.id]['tokens'][token]['url'])
            message = str(token) + "\n"
            update.message.reply_text(message)
    else:
        message = 'Ой, у тебя еще нет токенов( Ты можешь купить их, написав /buy\n'
        update.message.reply_text(message)


def sell_command(update, context):
    tockens_command(update, context)
    message = 'Чтобы продать напиши sell_<цена>_<токен>\n'
    update.message.reply_text(message)


def buy_command(update, context):
    message = "Вот видео~\n\n\n"
    update.message.reply_text(message)

    for key in market:
        context.bot.send_video(update.message.chat.id, market[key]['url'])
        message = 'Цена: ' + str(market[key]['price']) + '\n\n\n'
        message += 'Чтобы купить напиши buy_' + str(key) + '\n\n\n'
        update.message.reply_text(message, parse_mode="HTML")


def unknown_command(update, context):
    if 'buy' in update.message.text:
        mes = update.message.text.split('_')
        token = mes[-1]
        price = market[token]['price']

        if price <= users[update.effective_user.id]['balance']:
            message = 'Покупка успешна!\n'
            message += 'Вот ваш токен: ' + token + '\n'
            users[update.effective_user.id]['balance'] -= price
            users[market[token]["user_id"]]['balance'] += price

            users[update.effective_user.id]['tokens'][token] = {
                'url': market[token]['url'],
            }

            market.pop(token, None)
            message += 'Ваш баланс: ' + str(users[update.effective_user.id]['balance']) + '\n'
            update.message.reply_text(message)
        else:
            message = 'Недостаточно средств!\n'
            message += 'Ваш баланс: ' + str(users[update.effective_user.id]['balance']) + '\n'
            update.message.reply_text(message)
    elif 'sell' in update.message.text:
        mes = update.message.text.split('_')
        token = mes[-1]
        price = int(mes[-2])

        market[token] = {
            "price": price,
            "user_id": update.effective_user.id,
            'url': users[update.effective_user.id]['tokens'][token]['url']
        }

        message = 'Успешно выставлен на продажу!\n\n'
        update.message.reply_text(message)

    else:
        message = "Ой, а я не знаю такой команды. Напиши /help, что посмотреть список команд.\n"
        update.message.reply_text(message)


def info_command(update, context):
    message = "Информация о бот\n"
    update.message.reply_text(message)


def balance_command(update, context):
    message = 'Ваш баланс: ' + str(users[update.effective_user.id]['balance']) + '\n'
    update.message.reply_text(message)


token = "5079968253:AAEMl931K5GDBhagqM9bN_IqtF4I6ArNIEo"

updater = Updater(token, use_context=True)

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("tokens", tockens_command))
dispatcher.add_handler(CommandHandler("balance", balance_command))
dispatcher.add_handler(CommandHandler("help", help_command))
dispatcher.add_handler(CommandHandler("buy", buy_command))
dispatcher.add_handler(CommandHandler("sell", sell_command))
dispatcher.add_handler(CommandHandler("info", info_command))
dispatcher.add_handler(MessageHandler(Filters.text or Filters.command, unknown_command))

updater.start_polling()
updater.idle()
