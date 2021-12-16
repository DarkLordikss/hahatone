from telegram.ext import CommandHandler, MessageHandler, Filters, ConversationHandler
from telegram.ext import Updater, CallbackContext, CallbackQueryHandler
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove
from random import randint

print("Bot is working!")

test = ''

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
    },
    '234': {
        "user_id": 1233164455,
        "price": 15,
        "url": 'https://file-examples-com.github.io/uploads/2017/04/file_example_MP4_480_1_5MG.mp4'
    },
    '2345': {
        "user_id": 1233164455,
        "price": 32,
        "url": 'https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-mp4-file.mp4'
    },
    '113': {
        "user_id": 1233164455,
        "price": 14,
        "url": 'https://samplelib.com/lib/preview/mp4/sample-5s.mp4'
    },
    '452': {
        "user_id": 1233164455,
        "price": 10000000000000000,
        "url": 'https://filesamples.com/samples/video/mp4/sample_640x360.mp4'
    },
    '4567': {
        "user_id": 1233164455,
        "price": 27,
        "url": 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4'
    },
    '67584': {
        "user_id": 1233164455,
        "price": 29,
        "url": 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4'
    },
    '67584ewfwef': {
            "user_id": 1233164455,
            "price": 34,
            "url": 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerFun.mp4'
    },
    'h2sjkldaj': {
        "user_id": 1233164455,
        "price": 67,
        "url": 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerJoyrides.mp4'
    },
    'yutrie58': {
        "user_id": 1233164455,
        "price": 91,
        "url": 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerMeltdowns.mp4'
    },
    '876tghju': {
        "user_id": 1233164455,
        "price": 51,
        "url": 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/Sintel.mp4'
    },
    'oi87yhju': {
        "user_id": 1233164455,
        "price": 78,
        "url": 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/WhatCarCanYouGetForAGrand.mp4'
    },
    'loi87yhjuy7': {
        "user_id": 1233164455,
        "price": 23,
        "url": 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/WeAreGoingOnBullrun.mp4'
    },
    '9oki9iki': {
        "user_id": 1233164455,
        "price": 64,
        "url": 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/VolkswagenGTIReview.mp4'
    },
    '98uji8': {
        "user_id": 1233164455,
        "price": 59,
        "url": 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/TearsOfSteel.mp4'
    },
    'jhtgtgt66': {
        "user_id": 1233164455,
        "price": 61,
        "url": '"http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/SubaruOutbackOnStreetAndDirt.mp4'
    }
}

free_nft = {
    'djfidsjf': {
        "user_id": 1233164455,
        "price": 10,
        "url": 'http://techslides.com/demos/sample-videos/small.mp4'
    },
    '13n923f3': {
        "user_id": 1233164455,
        "price": 15,
        "url": 'https://file-examples-com.github.io/uploads/2017/04/file_example_MP4_480_1_5MG.mp4'
    },
    '23dh9831d': {
        "user_id": 1233164455,
        "price": 32,
        "url": 'https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-mp4-file.mp4'
    },
    '327dh92d': {
        "user_id": 1233164455,
        "price": 14,
        "url": 'https://samplelib.com/lib/preview/mp4/sample-5s.mp4'
    },
    '32d2893': {
        "user_id": 1233164455,
        "price": 100,
        "url": 'https://filesamples.com/samples/video/mp4/sample_640x360.mp4'
    },
    'fvbhgf66': {
        "user_id": 1233164455,
        "price": 100,
        "url": 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4'
    },
    '98765rfgh': {
        "user_id": 1233164455,
        "price": 100,
        "url": 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ElephantsDream.mp4'
    },
    '612ec': {
        "user_id": 1233164455,
        "price": 334,
        "url": 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerFun.mp4'
    },
    '612edb28=c': {
            "user_id": 1233164455,
            "price": 334,
            "url": 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerJoyrides.mp4'
    },
    '98yghji87': {
        "user_id": 1233164455,
        "price": 334,
        "url": 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerMeltdowns.mp4'
    },
    'oiuyg987': {
        "user_id": 1233164455,
        "price": 334,
        "url": 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/Sintel.mp4'
    },
    'oi8yhju': {
        "user_id": 1233164455,
        "price": 78,
        "url": 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/WhatCarCanYouGetForAGrand.mp4'
    },
    'loi8yhjuy7': {
        "user_id": 1233164455,
        "price": 23,
        "url": 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/WeAreGoingOnBullrun.mp4'
    },
    '9oi9iki': {
        "user_id": 1233164455,
        "price": 51,
        "url": 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/VolkswagenGTIReview.mp4'
    },
    '98ji8': {
        "user_id": 1233164455,
        "price": 51,
        "url": 'http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/TearsOfSteel.mp4'
    },
    'jhtgtgt6': {
        "user_id": 1233164455,
        "price": 51,
        "url": '"http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/SubaruOutbackOnStreetAndDirt.mp4'
    }
}


cursors = {

}

temp = {

}


def catcher(func):
    """Catching errors."""

    def catch(update: Update, context: CallbackContext):
        try:
            func(update, context)
        except Exception as ex:
            message = "*звуки сверчков*"
            update.message.reply_markdown_v2(message)

    return catch


@catcher
def reg_command(update, context):
    message = 'Пройдите регистрацию по ссылке test.com'
    update.message.reply_text(message)


@catcher
def start(update, context):
    print('START - ' + str(update.effective_user.id) + ' - ' + str(update.message.from_user['username']) + ' - ' + str(update.message.from_user['first_name']) + ' ' + str(update.message.from_user['last_name']))
    if not users.get(update.effective_user.id):
        users[update.effective_user.id] = {
            "balance": 100,
            "tokens": {}
        }
    if test == '':
        message = "Привет, я Оки Токен~\nДля авторизации введите auth_<токен_авторизации>.\nДля регистрации введите /reg\n"
        update.message.reply_text(message)
    else:
        message = "Привет, я Оки Токен~ Напиши /help, чтобы узнать больше."
        update.message.reply_text(message)


@catcher
def help_command(update, context):
    message = "Доступные команды:\n"
    message += "/start - Приветствие\n"
    message += "/buy - Купить NFT\n"
    message += "/sell - Продать NFT\n"
    message += "/info - Информация о боте\n"
    message += "/balance - Баланс\n"
    message += "/tokens - Твои токены\n"
    update.message.reply_text(message)
    print('HELP - ' + str(update.effective_user.id) + ' - ' + str(update.message.from_user['username']) + ' - ' + str(update.message.from_user['first_name']) + ' ' + str(update.message.from_user['last_name']))


@catcher
def tockens_command(update, context):
    print(users)
    print(users[update.effective_user.id])
    if users[update.effective_user.id]['tokens'] != {}:
        message = 'Вот твои токены~\n\n'
        update.message.reply_text(message)
        for token in users[update.effective_user.id]['tokens']:
            message = 'Токен: ' + str(token) + "\n"
            message += 'URL: ' + users[update.effective_user.id]['tokens'][token]['url'] + '\n'
            update.message.reply_text(message)
    else:
        message = 'Ой, у тебя еще нет токенов( Ты можешь купить их, написав /buy\n'
        update.message.reply_text(message)
    print('TOKENS - ' + str(update.effective_user.id) + ' - ' + str(update.message.from_user['username']) + ' - ' + str(update.message.from_user['first_name']) + ' ' + str(update.message.from_user['last_name']))


@catcher
def sell_command(update, context):
    message = 'Чтобы продать напиши sell_<цена>_<токен>\n'
    update.message.reply_text(message)
    print('SELL' + str(update.effective_user.id) + ' - ' + str(update.message.from_user['username']) + ' - ' + str(update.message.from_user['first_name']) + ' ' + str(update.message.from_user['last_name']))


@catcher
def unknown_command(update, context):
    if 'buy' in update.message.text:
        print('BUY -' + str(update.effective_user.id) + ' - ' + str(update.message.from_user['username']) + ' - ' + str(update.message.from_user['first_name']) + ' ' + str(update.message.from_user['last_name']))
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

        users[update.effective_user.id]['tokens'].pop(token)

        message = 'Успешно выставлен на продажу!\n\n'
        update.message.reply_text(message)

    elif 'auth' in update.message.text:
        global test
        test = update.message.text
        message = 'Авторизация прошла успешно!'
        update.message.reply_text(message)

    else:
        message = "Ой, а я не знаю такой команды. Напиши /help, что посмотреть список команд.\n"
        update.message.reply_text(message)


@catcher
def info_command(update, context):
    message = "Здравствуй!\n Я помогу тебе приобрести или продать NFT.\n"
    message += "P.S. При покупке ты помешь получить небольшой бонус от меня)"

    update.message.reply_text(message)
    print('INFO - ' + str(update.effective_user.id) + ' - ' + str(update.message.from_user['username']) + ' - ' + str(update.message.from_user['first_name']) + ' ' + str(update.message.from_user['last_name']))


@catcher
def balance_command(update, context):
    message = 'Ваш баланс: ' + str(users[update.effective_user.id]['balance']) + '\n'
    update.message.reply_text(message)
    print('BALANCE - ' + str(update.effective_user.id) + ' - ' + str(update.message.from_user['username']) + ' - ' + str(update.message.from_user['first_name']) + ' ' + str(update.message.from_user['last_name']))


@catcher
def buy(update: Update, context: CallbackContext) -> None:
    print('BUY - ' + str(update.effective_user.id) + ' - ' + str(update.message.from_user['username']) + ' - ' + str(update.message.from_user['first_name']) + ' ' + str(update.message.from_user['last_name']))
    cursor = cursors.get(update.effective_user.id, 0)

    if cursor >= len(market):
        cursor = 0

    if len(market) == 0:
        update.message.reply_text('Всё скупили =(')
        return

    token, value = list(market.items())[cursor]

    cursors[update.effective_user.id] = (cursor + 1) % len(market)

    keyboard = [
        [
            InlineKeyboardButton("Назад", callback_data='back'),
            InlineKeyboardButton("Дальше", callback_data='next'),
        ],
        [InlineKeyboardButton("Купить", callback_data='buy_' + token)],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    message = 'Токен: ' + str(token) + '\n'
    message += 'Цена: ' + str(value['price']) + ' кредитов\n'
    message += 'URL: ' + value['url'] + '\n'

    update.message.reply_text(message)
    update.message.reply_text('Сделайте выбор', reply_markup=reply_markup)


@catcher
def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    query.answer()

    cursor = cursors.get(update.effective_user.id, 0)

    query.edit_message_text(text=f"Выбрано: {query.data}")

    if "buy" in query.data:
        mes = query.data.split('_')
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

            if randint(0, 5) == 3:
                message += '\n\n\nВам повезло! Во получаете еще один NFT бесплатно!\n'

                r = randint(0, len(free_nft) - 1)
                t, v = list(free_nft.items())[r]
                free_nft.pop(t, None)

                users[update.effective_user.id]['tokens'][t] = v

            market.pop(token, None)
            message += 'Ваш баланс: ' + str(users[update.effective_user.id]['balance']) + '\n'
            query.message.reply_text(message)
        else:
            message = 'Недостаточно средств!\n'
            message += 'Ваш баланс: ' + str(users[update.effective_user.id]['balance']) + '\n'
            query.message.reply_text(message)

        return

    if query.data == "next":
        cursor += 1
    elif query.data == "back":
        cursor -= 1

    cursor = cursor % len(market)
    cursors[update.effective_user.id] = cursor

    if len(market) == 0:
        update.message.reply_text('Всё скупили =(')
        return

    token, value = list(market.items())[cursor]

    message = 'Токен: ' + str(token) + '\n'
    message += 'Цена: ' + str(value['price']) + ' кредитов\n'
    message += 'URL: ' + value['url'] + '\n'
    query.message.reply_text(message)

    keyboard = [
        [
            InlineKeyboardButton("Назад", callback_data='back'),
            InlineKeyboardButton("Дальше", callback_data='next'),
        ],
        [InlineKeyboardButton("Купить", callback_data='buy_' + token)],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    message = 'Токен: ' + str(token) + '\n'
    message += 'Цена: ' + str(value['price']) + ' кредитов\n'
    message += 'URL: ' + value['url'] + '\n'

    query.message.reply_text('Сделайте выбор', reply_markup=reply_markup)


TOKEN, URL, PRICE = range(3)


@catcher
def add_token(update: Update, context: CallbackContext) -> int:
    print('ADD - ' + str(update.effective_user.id) + ' - ' + str(update.message.from_user['username']) + ' - ' + str(update.message.from_user['first_name']) + ' ' + str(update.message.from_user['last_name']))
    user = update.message.from_user
    update.message.reply_text(
        'Вставьте NFT токен'
    )

    return TOKEN


@catcher
def add_url(update: Update, context: CallbackContext) -> int:
    temp[update.effective_user.id] = {}
    temp[update.effective_user.id]["token"] = update.message.text

    update.message.reply_text(
        'Вставьте ссылку на ваше видео',
        reply_markup=ReplyKeyboardRemove(),
    )

    return URL


@catcher
def add_price(update: Update, context: CallbackContext) -> int:
    temp[update.effective_user.id]["url"] = update.message.text

    update.message.reply_text(
        'Введите цену, за которую вы хотите продать свой токен'
    )

    return PRICE


@catcher
def done_conv(update: Update, context: CallbackContext) -> int:
    try:
        price = int(update.message.text)
        token = temp[update.effective_user.id]["token"]
        url = temp[update.effective_user.id]["url"]

        market[token] = {
            "user_id": update.effective_user.id,
            "price": price,
            "url": url
        }

        temp.pop(update.effective_user.id, None)

        update.message.reply_text(
            'Успешно! Выставили ваш токен на продажу'
        )
    except Exception as e:
        update.message.reply_text(
            'Не смогли обработать, попробуйте снова'
        )

    return ConversationHandler.END


@catcher
def cancel_conv(update: Update, context: CallbackContext) -> int:
    """Cancels and ends the conversation."""
    update.message.reply_text(
        'Понял, отмена', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


if __name__ == "__main__":
    token = "5079968253:AAEMl931K5GDBhagqM9bN_IqtF4I6ArNIEo"

    updater = Updater(token, use_context=True)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("tokens", tockens_command))
    dispatcher.add_handler(CommandHandler("balance", balance_command))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("sell", sell_command))
    dispatcher.add_handler(CommandHandler("info", info_command))
    dispatcher.add_handler(CommandHandler("reg", reg_command))

    dispatcher.add_handler(CommandHandler('buy', buy))
    dispatcher.add_handler(CallbackQueryHandler(button))

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('add', add_token)],
        states={
            TOKEN: [MessageHandler(Filters.text & ~Filters.command, add_url)],
            URL: [MessageHandler(Filters.text & ~Filters.command, add_price)],
            PRICE: [MessageHandler(Filters.text & ~Filters.command, done_conv)],
        },
        fallbacks=[CommandHandler('cancel', cancel_conv)],
    )

    dispatcher.add_handler(conv_handler)

    dispatcher.add_handler(MessageHandler(Filters.text or Filters.command, unknown_command))

    updater.start_polling()
    updater.idle()
