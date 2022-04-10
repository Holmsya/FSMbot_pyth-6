from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage    # позволяет хранить данные в оперативной памяти

API_TOKEN = '5191483081:AAF2Mf94vXaoMyA7kf7pZ2JpKGIYXf5_soc'

storage = MemoryStorage()

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)
