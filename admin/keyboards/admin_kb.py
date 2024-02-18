from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

main_kb = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True).add(
    KeyboardButton(text='Mentor tahrirlash'),
    KeyboardButton(text="E'lon"),
    KeyboardButton(text='Parol tahrirlash'),
    KeyboardButton(text='Admin tahrirlash'),
    KeyboardButton(text='Mentorlar analitikasi'),
    KeyboardButton(text='🔝 Asosiy Menyu'),
)

edit_mentor_kb = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True).add(
    KeyboardButton(text="qo'shish"),
    KeyboardButton(text="o'chirish"),
    KeyboardButton(text='🔙 Ortga',)
)


edit_admin_kb = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True).add(
    KeyboardButton(text="admin qo'shish"),
    KeyboardButton(text='admin o\'chirish'),
    KeyboardButton(text='🔙 Ortga'),
)

edit_password_kb = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True).add(
    KeyboardButton(text='parolni tahrirlash'),
    KeyboardButton(text='🔙 Ortga'),
)


main_analysis = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True).add(
    KeyboardButton(text='Analaitikani ko\'rishga dostup berish'),
    KeyboardButton(text='Analitikani ko\'rish'),
    KeyboardButton(text='🔙 Ortga'),
)

access_user_kb = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True).add(
    KeyboardButton(text='ruxsat qo\'shish'),
    KeyboardButton(text='ruxsatni o\'chirish'),
    KeyboardButton(text='🔙 Ortga.'),
)

view_analysis_kb = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True).add(
    # KeyboardButton(text='Haftalik'),
    KeyboardButton(text='Kirish'),
    KeyboardButton(text='🔙 Ortga.'),
)
