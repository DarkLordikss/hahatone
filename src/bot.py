from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

print("Bot is working!")

users = {
    1233164455: {
        "balance": 100,
        "tokens": []
    }
}
market = {
    '123': {
        "user_id": 1233164455,
        "price": 10,
        "name": 'Hook'
    },
    '234': {
        "user_id": 1233164455,
        "price": 15,
        "name": 'Not hook'
    }
}


def start(update, context):
    if not users.get(update.effective_user.id):
        users[update.effective_user.id] = {
            "balance": 100,
            "tokens": []
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
    if users[update.effective_user.id]['tokens'] != []:
        message = 'Вот твои токены~\n\n'
        for token in users[update.effective_user.id]['tokens']:
            message += str(token) + "\n"
            # for key in i:
            #     message += key
            #     message += ' - ' + str(i[key]) + ' кредитов\n'
            #     break
    else:
        message = 'Ой, у тебя еще нет токенов( Ты можешь купить их, написав /buy\n'
    update.message.reply_text(message)


def buy_command(update, context):
    message = "Выберите категорию:\n"
    message += "/video - Видео\n"
    message += "/game - Игровые предметы\n"
    message += "/audio - Аудиофайлы\n"
    message += "/gif - GIF-изображения\n"
    update.message.reply_text(message)


def sell_command(update, context):
    tockens_command(update, context)
    message = 'Чтобы продать напиши sell_<цена>_<токен>\n'
    update.message.reply_text(message)


def gif_command(update, context):
    message = "Вот gif~\n"
    update.message.reply_text(message)


def audio_command(update, context):
    message = "Вот звуки~\n"
    update.message.reply_text(message)


def video_command(update, context):
    message = "Вот видео~\n"
    update.message.reply_text(message)


def game_command(update, context):
    message = "Вот игровые предметы~\n"
    update.message.reply_text(message)

    for key in market:
        message = 'Название : ' + market[key]['name'] + '\n\n'
        message += 'Цена:' + str(market[key]['price']) + '\n\n'
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
            users[update.effective_user.id]['tokens'].append(token)

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
            "user_id": update.effective_user.id
            "name":
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
dispatcher.add_handler(CommandHandler("audio", audio_command))
dispatcher.add_handler(CommandHandler("game", game_command))
dispatcher.add_handler(CommandHandler("gif", gif_command))
dispatcher.add_handler(CommandHandler("video", video_command))
dispatcher.add_handler(CommandHandler("info", info_command))
dispatcher.add_handler(MessageHandler(Filters.text or Filters.command, unknown_command))

updater.start_polling()
updater.idle()
