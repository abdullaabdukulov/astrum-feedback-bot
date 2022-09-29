import json

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from keyboards.default.menu_keyboard import menu
from loader import dp


def open_password():
    f = open('/Users/student/Desktop/bot/My_Mentor_feedback_bot/data/password.json', 'r')
    passwords = json.load(f)
    f.close()
    return passwords


print(open_password())


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    await state.set_state("pas")
    await message.answer(f"Assalomu Alaykum\nXush kelibsiz {message.from_user.full_name}!")
    await message.answer(f"Bu Astrum mentorlariga\nfeedback berish uchun bot\nSiz Astrumda ishlashiingiz yoki "
                         f"o'qishingizni tasdiqlash uchun Mac kamputerlar parolini kiriting iltimos.")


@dp.message_handler(state='pas', text=open_password())
async def pas_chek(msg: types.Message, state: FSMContext):
    await msg.reply("Parol to'g'ri ✔️", reply_markup=menu)
    await state.finish()


@dp.message_handler(state='pas')
async def pas_chek(msg: types.Message):
    await msg.reply("Iltimos parolni to'g'ri kiriting to'g'ri kiriting.")