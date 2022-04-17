from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove


async def rm_kb(message: types.Message):
    await message.reply("Keyboard has been removed.", reply_markup=ReplyKeyboardRemove())


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(rm_kb, Text(equals='Remove keyboard', ignore_case=True))
