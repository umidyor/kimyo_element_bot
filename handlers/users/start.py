from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.language import languages_keyboard
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, hurmatli {message.from_user.first_name}, Siz buyruqlardan birini tanlab tilni tanlang va element nomini yozing✏️Men shu element haqida ma'lumot beraman🤗", reply_markup=languages_keyboard)

