from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[[
            KeyboardButton(text="Mentorga feedback qoldirish")
        ]],
    resize_keyboard=True, one_time_keyboard=True
)
