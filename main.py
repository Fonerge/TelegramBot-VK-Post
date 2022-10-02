import os
import vk_api
import telebot
import requests
import config as c
import keyboard as kb
from telebot import types

session = vk_api.VkApi(token=c.ACCESS_TOKEN)
vk = session.get_api()

bot = telebot.TeleBot(c.TOKEN, parse_mode='HTML')

id_barah_1 = "-" + str(vk.groups.getById(group_id = 'vapemarketperm')[0]['id']) # VAPE БАРАХОЛКА | ПЕРМЬ
id_barah_2 = "-" + str(vk.groups.getById(group_id = 'baraholkavaperm')[0]['id']) # Барахолка Вейп | Кальянов | Пермь
id_barah_3 = "-" + str(vk.groups.getById(group_id = 'vapedrip')[0]['id']) # Вейп Барахолка № 1 в Перми | IQOS | VAPE
id_barah_4 = "-" + str(vk.groups.getById(group_id = 'vape_perm_1')[0]['id']) # VAPE ВЕЙП Барахолка Пермь
id_barah_5 = "-" + str(vk.groups.getById(group_id = '59tobaccoshop')[0]['id']) # <БАРАХОЛКА ВЕЙП/КАЛЬЯН ПЕРМЬ>VAPE&HOOKAH
id_barah_6 = "-" + str(vk.groups.getById(group_id = 'club140086571')[0]['id']) # VAPE барахолка Пермь (вейп)
id_barah_7 = "-" + str(vk.groups.getById(group_id = 'vapebaraholkapermi')[0]['id']) # VAPE БАРАХОЛКА ПЕРМЬ | КАЛЬЯН
id_barah_8 = "-" + str(vk.groups.getById(group_id = 'permvapebaraholka')[0]['id']) # | VAPE BARAHOLKA |Пермь| Вейп барахолка | VAPE
id_barah_9 = "-" + str(vk.groups.getById(group_id = 'vape59prm')[0]['id']) # Vape / Вейп / Пермь / Барахолка
id_barah_10 = "-" + str(vk.groups.getById(group_id = 'sell_vape_perm')[0]['id']) # Вейп | VAPE Барахолка Пермь

@bot.message_handler(commands=['start'])
def send_welcome(message):
	name = message.from_user.first_name
	bot.send_message(message.chat.id, "Привет, {0}!\nЯ бот, раскидывающий ваш товар на барахолки.\nНажмите <a href=''>/raskid</a>, чтобы сделать пост.".format(name),
		reply_markup = kb.markup)

@bot.message_handler(commands=['raskid'])
def handle_text(message):
	bot.send_message(message.from_user.id, "Введите текст.", reply_markup=kb.markup_1)

	@bot.message_handler(content_types=['text'])
	def handle_text(message):
		if message.text == 'Отмена 🙅‍♂️':
			bot.send_message(message.chat.id, "Действие отменено.\n\nНажмите <a href="">/raskid</a>, чтобы сделать пост заново.", reply_markup=kb.markup)
		else:
			global txt
			txt = message.text
			bot.send_message(message.chat.id, "Отправьте фото.")

	@bot.message_handler(content_types=['photo'])
	def send_file_photo(message):

		# получение фото пользвателя и загрузка на сервер.

		photo_id = message.photo[-1].file_id
		file_photo = bot.get_file(photo_id)
		file_name, file_extension = os.path.splitext(file_photo.file_path)
		downloaded_file_photo = bot.download_file(file_photo.file_path)
		src = 'photos/' + photo_id + file_extension
		with open(src, 'wb') as new_file:
			new_file.write(downloaded_file_photo)
		bot.send_message(message.from_user.id, '<i>Ожидайте...</i>', parse_mode='HTML')
		#1 	
		# upload_url =  vk.photos.getWallUploadServer(owner_id=id_barah_1)['upload_url']
		# request = requests.post(upload_url, files = {'file': open(src, 'rb')})
		# save_wall_photo = vk.photos.saveWallPhoto(owner_id = id_barah_1,
		#     						photo = request.json()['photo'],
		#     						server = request.json()['server'],
		#     						hash = request.json()['hash'])
		# saved_photo = "photo" + str(save_wall_photo[0]['owner_id']) + "_" + str(save_wall_photo[0]['id'])
		# vk.wall.post(owner_id = id_barah_1, attachments = saved_photo, message = txt)
		#2
		upload_url =  vk.photos.getWallUploadServer(owner_id=id_barah_2)['upload_url']
		request = requests.post(upload_url, files = {'file': open(src, 'rb')})
		save_wall_photo = vk.photos.saveWallPhoto(owner_id = id_barah_2,
		    						photo = request.json()['photo'],
		    						server = request.json()['server'],
		    						hash = request.json()['hash'])
		saved_photo = "photo" + str(save_wall_photo[0]['owner_id']) + "_" + str(save_wall_photo[0]['id'])
		vk.wall.post(owner_id = id_barah_2, attachments = saved_photo, message = txt)
		#3
		# upload_url =  vk.photos.getWallUploadServer(owner_id=id_barah_3)['upload_url']
		# request = requests.post(upload_url, files = {'file': open(src, 'rb')})
		# save_wall_photo = vk.photos.saveWallPhoto(owner_id = id_barah_3,
		#     						photo = request.json()['photo'],
		#     						server = request.json()['server'],
		#     						hash = request.json()['hash'])
		# saved_photo = "photo" + str(save_wall_photo[0]['owner_id']) + "_" + str(save_wall_photo[0]['id'])
		# vk.wall.post(owner_id = id_barah_3, attachments = saved_photo, message = txt)
		#4
		upload_url =  vk.photos.getWallUploadServer(owner_id=id_barah_4)['upload_url']
		request = requests.post(upload_url, files = {'file': open(src, 'rb')})
		save_wall_photo = vk.photos.saveWallPhoto(owner_id = id_barah_4,
		    						photo = request.json()['photo'],
		    						server = request.json()['server'],
		     						hash = request.json()['hash'])
		saved_photo = "photo" + str(save_wall_photo[0]['owner_id']) + "_" + str(save_wall_photo[0]['id'])
		vk.wall.post(owner_id = id_barah_4, attachments = saved_photo, message = txt)
		#5
		upload_url =  vk.photos.getWallUploadServer(owner_id=id_barah_5)['upload_url']
		request = requests.post(upload_url, files = {'file': open(src, 'rb')})
		save_wall_photo = vk.photos.saveWallPhoto(owner_id = id_barah_5,
		    						photo = request.json()['photo'],
		    						server = request.json()['server'],
		    						hash = request.json()['hash'])
		saved_photo = "photo" + str(save_wall_photo[0]['owner_id']) + "_" + str(save_wall_photo[0]['id'])
		vk.wall.post(owner_id = id_barah_5, attachments = saved_photo, message = txt)
		#6
		upload_url =  vk.photos.getWallUploadServer(owner_id=id_barah_6)['upload_url']
		request = requests.post(upload_url, files = {'file': open(src, 'rb')})
		save_wall_photo = vk.photos.saveWallPhoto(owner_id = id_barah_6,
		    						photo = request.json()['photo'],
		    						server = request.json()['server'],
		    						hash = request.json()['hash'])
		saved_photo = "photo" + str(save_wall_photo[0]['owner_id']) + "_" + str(save_wall_photo[0]['id'])
		vk.wall.post(owner_id = id_barah_6, attachments = saved_photo, message = txt)
		#7
		upload_url =  vk.photos.getWallUploadServer(owner_id=id_barah_7)['upload_url']
		request = requests.post(upload_url, files = {'file': open(src, 'rb')})
		save_wall_photo = vk.photos.saveWallPhoto(owner_id = id_barah_7,
		    						photo = request.json()['photo'],
		    						server = request.json()['server'],
		    						hash = request.json()['hash'])
		saved_photo = "photo" + str(save_wall_photo[0]['owner_id']) + "_" + str(save_wall_photo[0]['id'])
		vk.wall.post(owner_id = id_barah_7, attachments = saved_photo, message = txt)
		#8
		upload_url =  vk.photos.getWallUploadServer(owner_id=id_barah_8)['upload_url']
		request = requests.post(upload_url, files = {'file': open(src, 'rb')})
		save_wall_photo = vk.photos.saveWallPhoto(owner_id = id_barah_8,
		    						photo = request.json()['photo'],
		    						server = request.json()['server'],
		    						hash = request.json()['hash'])
		saved_photo = "photo" + str(save_wall_photo[0]['owner_id']) + "_" + str(save_wall_photo[0]['id'])
		vk.wall.post(owner_id = id_barah_8, attachments = saved_photo, message = txt)
		#9
		upload_url =  vk.photos.getWallUploadServer(owner_id=id_barah_9)['upload_url']
		request = requests.post(upload_url, files = {'file': open(src, 'rb')})
		save_wall_photo = vk.photos.saveWallPhoto(owner_id = id_barah_9,
		    						photo = request.json()['photo'],
		    						server = request.json()['server'],
		     						hash = request.json()['hash'])
		saved_photo = "photo" + str(save_wall_photo[0]['owner_id']) + "_" + str(save_wall_photo[0]['id'])
		vk.wall.post(owner_id = id_barah_9, attachments = saved_photo, message = txt)
		#10
		upload_url =  vk.photos.getWallUploadServer(owner_id=id_barah_10)['upload_url']
		request = requests.post(upload_url, files = {'file': open(src, 'rb')})
		save_wall_photo = vk.photos.saveWallPhoto(owner_id = id_barah_10,
		    						photo = request.json()['photo'],
		    						server = request.json()['server'],
		    						hash = request.json()['hash'])
		saved_photo = "photo" + str(save_wall_photo[0]['owner_id']) + "_" + str(save_wall_photo[0]['id'])
		vk.wall.post(owner_id = id_barah_10, attachments = saved_photo, message = txt)

		bot.send_message(message.chat.id, 'Ваш пост успешно отправлен.\n\nНажмите <a href="">/raskid</a>, чтобы сделать новый пост.',
		reply_markup=kb.markup)
		
bot.infinity_polling()