import json
from pathlib import Path

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from keyboards.default.menu_keyboard import menu
from loader import dp

BASE_DIR = Path(__file__).resolve().parent.parent.parent

json_file = f"{BASE_DIR}/data/password.json"


def open_password():
    with open(json_file, 'r') as f:
        passwords = json.load(f)
    return passwords


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    await state.set_state("pas")
    await message.answer(f"Assalomu Alaykum\nXush kelibsiz {message.from_user.full_name}!")
    await message.answer(f"Bu Astrum mentorlariga\nfeedback berish uchun bot\nSiz Astrumda ishlashiingiz yoki "
                         f"o'qishingizni tasdiqlash uchun Mac kamputerlar parolini kiriting iltimos.")


@dp.message_handler(state='pas')
async def pas_chek(msg: types.Message, state: FSMContext):
    passwords = open_password()
    if msg.text in passwords:
        await msg.reply("Parol to'g'ri ✔️", reply_markup=menu)
        await state.finish()
    else:
        await msg.reply("Iltimos parolni to'g'ri kiriting.")


def register_handler_start(db: Dispatcher):
    dp.message_handler(bot_start, commands=CommandStart)