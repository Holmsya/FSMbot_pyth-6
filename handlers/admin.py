from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()


async def upload(message: types.Message):
    await FSMAdmin.photo.set()
    await message.reply("Upload photo")


async def upload_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply("Insert name")


async def insert_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.reply("Insert description")


async def insert_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
        await message.answer(str(data))
    await state.finish()


async def cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply("OK")


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(upload, commands=['upload'], state=None)
    dp.register_message_handler(cancel, commands=['cancel'], state="*")
    dp.register_message_handler(cancel, Text(equals='cancel', ignore_case=True), state="*")
    dp.register_message_handler(upload_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(insert_name, state=FSMAdmin.name)
    dp.register_message_handler(insert_description, state=FSMAdmin.description)
