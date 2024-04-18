import telebot
import shutil
from data import token
from data import chat_id
TOKEN = token
RECEIVER_ID = chat_id
FILE_PATH = '/etc/x-ui/x-ui.db'

def send_message(message):
    bot = telebot.TeleBot(TOKEN)
    bot.send_message(RECEIVER_ID, message)

def send_file():
    bot = telebot.TeleBot(TOKEN)
    with open(FILE_PATH, 'rb') as f:
        bot.send_document(RECEIVER_ID, f)

def copy_and_send_file():
    try:
        shutil.copy2(FILE_PATH, 'xui.db')
        send_file()
        send_message("فایل با موفقیت کپی شد و ارسال شد.")
    except Exception as e:
        send_message(f"خطا در کپی کردن فایل: {str(e)}")

copy_and_send_file()
