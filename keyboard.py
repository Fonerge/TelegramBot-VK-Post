import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

btn_raskid = types.KeyboardButton('/raskid')
markup = types.ReplyKeyboardMarkup(resize_keyboard = True).add(btn_raskid)

btn_cancel = types.KeyboardButton('Отмена 🙅‍♂️')
markup_1 = types.ReplyKeyboardMarkup(resize_keyboard = True).add(btn_cancel)