import telebot
from PIL import Image, ImageOps
import requests
import io
TOKEN = '6532943541:AAGBaSBTq7nLExpI35L47vcGz08pMMxik_8'#token
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
	bot.reply_to(message,"*ارسل الصوره*",parse_mode="markdownV2")
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    file_info = bot.get_file(message.photo[-1].file_id)
    file_path = file_info.file_path
    file_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    file = requests.get(file_url)
    image = Image.open(io.BytesIO(file.content))
    image = ImageOps.grayscale(image)
    image.save('modified_image.jpg')
    with open('modified_image.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id,photo)
print("The Code is runing...")       
bot.polling()
