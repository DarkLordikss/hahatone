from telegram.ext import Updater, CommandHandler

print("Bot is working!")


def on_start(update, context):
	chat = update.effective_chat
	context.bot.send_message(chat_id=chat.id, text="Привет, я Валютный бот")


token = "2033151314:AAGm_T4a80d_hydMQzocj6KY4rn-pd4wFIQ"

updater = Updater(token, use_context=True)

dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", on_start))

updater.start_polling()
updater.idle()
