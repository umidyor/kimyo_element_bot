from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from keyboards.inline.callback_data import language_callback

languages_keyboard = InlineKeyboardMarkup()
languages_keyboard.add(
    InlineKeyboardButton("🇺🇿 Uzbek", callback_data=language_callback.new(lang="uz")),
    InlineKeyboardButton("🇬🇧 English", callback_data=language_callback.new(lang="en")),
)

change_language = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True).add(
    KeyboardButton(text='Tilni Tanlang / Choose Language)'),
)