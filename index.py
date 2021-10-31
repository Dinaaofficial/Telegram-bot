import os
import telebot


bot = telebot.TeleBot("YOUR API HERE")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm DINA BOT")


bot.polling()
