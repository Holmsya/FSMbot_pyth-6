from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button_upload = KeyboardButton('Upload')
button_rm_kb = KeyboardButton('Remove keyboard')
button_contact = KeyboardButton('Send my contact', request_contact=True)
button_location = KeyboardButton('Send my location', request_location=True)

kb_main = ReplyKeyboardMarkup(resize_keyboard=True)  # добавить one_time_keyboard = True для того,
                                                     # чтобы спрятать после нажатия
kb_main.add(button_upload).row(button_contact, button_location).add(button_rm_kb)

button_cancel = KeyboardButton('cancel')

kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True)
kb_cancel.add(button_cancel)
