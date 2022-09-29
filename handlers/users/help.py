from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/admin - Admin panelga kirish",
            "/analysis - Mentorlar analitikasiga kirish",
            "/direction - Yo'nalishni o'zgartirish")
    await message.answer("\n".join(text))
