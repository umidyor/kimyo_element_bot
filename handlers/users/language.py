from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandHelp
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery, Message

from handlers.users.data_clean import search_data
from keyboards.inline.callback_data import language_callback
from keyboards.inline.language import languages_keyboard
from loader import dp


# Define the states for the conversation
class ElementInput(StatesGroup):
    waiting_for_element_name = State()


# Define the language selection handler
@dp.callback_query_handler(language_callback.filter())
async def language_selection_handler(callback_query: CallbackQuery, state: FSMContext, callback_data: dict):
    # Set the language for the user
    language = callback_data["lang"]
    await state.update_data(language=language)

    # Ask the user to input the element name
    await ElementInput.waiting_for_element_name.set()
    if language == 'uz':
        await callback_query.message.answer("Istagan kimyoviy elementingizni nomini yoki formulasini yozing:")
    else:
        await callback_query.message.answer("Type the name or formula of the element you want:")


# Define the element input handler
@dp.message_handler(state=ElementInput.waiting_for_element_name)
async def element_input_handler(message: Message, state: FSMContext):
    # Get the language and element name from the user's message
    language = (await state.get_data())["language"]
    element_name = message.text
    if element_name == '/start':
        await state.finish()
        await message.answer(f"Hurmatli {message.from_user.first_name}, Siz buyruqlardan birini tanlab tilni tanlang va element nomini yozing✏️Men shu element haqida ma'lumot beraman🤗",reply_markup=languages_keyboard)
    # Reply to the user based on their input
    if element_name == '/help':
        # End the conversation
        await state.finish()
        await message.answer("Tilni almashtirish(Change language):", reply_markup=languages_keyboard)
    else:
        if language == "uz":
            reply_text = search_data(element_name, lang=language)
        else:
            try:
                await message.answer(search_data(element_name, lang=language)['about'])
                reply_text = search_data(element_name, lang=language)['summary']
            except:
                reply_text = f"It's a pity😕 There is no information❌ about this {element_name} or you have made a syntax error."
        await message.answer(reply_text)



@dp.message_handler(text='Tilni Tanlang / Choose Language')
async def set_language(message: Message, state: FSMContext):
    # Ask the user to choose a language
    await message.answer('Choose a language / Tilni tanlang:', reply_markup=languages_keyboard)

    # Set the state to waiting for the language selection
    await ElementInput.waiting_for_element_name.set()

    # Store the current state in the context to be able to return to it later
    await state.set_state('previous_state')
