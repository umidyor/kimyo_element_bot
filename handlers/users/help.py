from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from .language import languages_keyboard
from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):

    await message.answer("Tilni almashtirish(Change language):",reply_markup=languages_keyboard)
