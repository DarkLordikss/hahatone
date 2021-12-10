from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

print("Bot is working!")


def start(update, context):
	chat = update.effective_chat
	context.bot.send_message(chat_id=chat.id, text="Привет, я Оки Токен~ Напиши /help, чтобы узнать больше.")


def help_command(update, context):
	chat = update.effective_chat
	message = "Доступные команды:\n"
	message += "/start - Приветствие\n"
	message += "/buy - Купить NFT\n"
	message += "/sell - Продать NFT\n"
	update.message.reply_text(message)


def buy_command(update, context):
	chat = update.effective_chat
	message = "Выберите категорию:\n"
	message += "/video - Видео\n"
	message += "/img - Изображения\n"
	message += "/audio - Аудиофайлы\n"
	message += "/gif - GIF-изображения\n"
	update.message.reply_text(message)


def sell_command(update, context):
	chat = update.effective_chat
	message = "Вот твои NFT~\n"
	update.message.reply_text(message)


def gif_command(update, context):
	chat = update.effective_chat
	message = "Вот gif~\n"
	update.message.reply_text(message)


def audio_command(update, context):
	chat = update.effective_chat
	message = "Вот звуки~\n"
	update.message.reply_text(message)


def video_command(update, context):
	chat = update.effective_chat
	message = "Вот видео~\n"
	update.message.reply_text(message)


def img_command(update, context):
	chat = update.effective_chat
	message = "Вот видео~\n"
	update.message.reply_text(message)


def unknown_command(update, context):
	chat = update.effective_chat
	message = "Вот картинки" \
			  "\n"
	update.message.reply_text(message)


token = "5079968253:AAEMl931K5GDBhagqM9bN_IqtF4I6ArNIEo"

updater = Updater(token, use_context=True)

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", help_command))
dispatcher.add_handler(CommandHandler("buy", buy_command))
dispatcher.add_handler(CommandHandler("sell", sell_command))
dispatcher.add_handler(CommandHandler("audio", audio_command))
dispatcher.add_handler(CommandHandler("img", img_command))
dispatcher.add_handler(CommandHandler("gif", gif_command))
dispatcher.add_handler(CommandHandler("video", video_command))
dispatcher.add_handler(MessageHandler(Filters.text and ~Filters.command, unknown_command))

updater.start_polling()
updater.idle()
