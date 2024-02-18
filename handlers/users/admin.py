from aiogram import types

from data import config
from keyboards.default.menu_keyboard import menu
from loader import dp

admins = config.ADMINS


@dp.message_handler(chat_id=admins, commands="start")
async def admins_answer(msg: types.Message):
    await msg.answer(f"Assalomu Alaykum\nXush kelibsiz SupperUser {msg.from_user.full_name}", reply_markup=menu)

