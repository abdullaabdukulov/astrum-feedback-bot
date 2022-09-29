from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.query_data import mentors_datas
from keyboards.inline.callback_data import data, full, soft, feed1, feed2, feed3

yonalish = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Data Science", callback_data="DS"),
            InlineKeyboardButton(text="Full Stack", callback_data="FS"),
            InlineKeyboardButton(text="Software Engineering", callback_data="SE"),
        ],
        [
            InlineKeyboardButton(text="🔙 Ortga", callback_data="back_menu"),
        ]
    ])

beck_menu = InlineKeyboardButton(text="🔙 Ortga", callback_data="back_menu")
beck_mentor = InlineKeyboardButton(text="🔙 Ortga", callback_data="back_mentor")
beck_feed3 = InlineKeyboardButton(text="🔙 Ortga", callback_data="back_feed3")


def d_mentors():
    d_mentors = {}
    for i in mentors_datas():
        if i[1] == 'DS':
            d_mentors[i[0]] = i[0]
    return d_mentors


def f_mentors():
    f_mentors = {}
    for i in mentors_datas():
        if i[1] == 'FS':
            f_mentors[i[0]] = i[0]
    return f_mentors


def s_mentors():
    s_mentors = {}
    for i in mentors_datas():
        if i[1] == 'SE':
            s_mentors[i[0]] = i[0]
    return s_mentors


beck_der = InlineKeyboardButton(text="🔙 Ortga", callback_data="back_der")
beck_mentor = InlineKeyboardButton(text="🔙 Ortga", callback_data="back_mentor")
beck_feed3 = InlineKeyboardButton(text="🔙 Ortga", callback_data="back_feed3")

# bu data sience mentorlar uchuun
def mentors_data():
    mentors_data = InlineKeyboardMarkup(row_width=1)
    for k, v in d_mentors().items():
        mentors_data.insert(InlineKeyboardButton(text=k, callback_data=data.new(item_name=v)))
    mentors_data.insert(beck_menu)
    return mentors_data


# bu full stack mentorlar uchun
def mentors_full():
    mentors_full = InlineKeyboardMarkup(row_width=1)
    for key, value in f_mentors().items():
        mentors_full.insert(InlineKeyboardButton(text=key, callback_data=full.new(item_name=value)))
    mentors_full.insert(beck_menu)
    return mentors_full


# bu softwer mentorlar uchun
def mentors_soft():
    mentors_soft = InlineKeyboardMarkup(row_width=1)
    for key, value in s_mentors().items():
        mentors_soft.insert(InlineKeyboardButton(text=key, callback_data=soft.new(item_name=value)))
    mentors_soft.insert(beck_menu)
    return mentors_soft


#########################################

feedback3 = {
    "😐 Qoniqarli": "Qoniqarli",
    "😊 Namunali": "Namunali",
    "☹️ Qoniqarsiz": "Qoniqarsiz"
}
feedback_de3 = InlineKeyboardMarkup(row_width=1)
for k, v in feedback3.items():
    feedback_de3.insert(InlineKeyboardButton(text=k, callback_data=v))
feedback_de3.insert(beck_mentor)


feedback_q_li1 = {
    "1) Mentor o'z vaqtida ish joyida": " Mentor o'z vaqtida ish joyida",
    "2) Mentor muomilasi yaxshi": "Mentor muomilasi yaxshi",
    "3) Mentor qiziqarli usulda taqdimot qilib tushuntirdi" : "Mentor qiziqarli usulda taqdimot qilib tushuntirdi"
}
feedback_q_li = InlineKeyboardMarkup(row_width=1)
for k, v in feedback_q_li1.items():
    feedback_q_li.insert(InlineKeyboardButton(text=k,  callback_data=feed1.new(item_feed=v)))
feedback_q_li.insert(beck_feed3)

feedback_n_li1 = {
    "1) Mentor barcha savoimga javob berdi": "Mentor barcha savoimga javob berdi",
    "2) Mentor juda ham yaxshi tushuntirdi": "Mentor juda ham yaxshi tushuntirdi",
    "3) Mentor yangicha usulda taqdimot qilib tushuntirdi": "Mentor yangicha usulda taqdimot qilib tushuntirdi"
}
feedback_n_li = InlineKeyboardMarkup(row_width=1)
for k, v in feedback_n_li1.items():
    feedback_n_li.insert(InlineKeyboardButton(text=k,  callback_data=feed2.new(item_feed=v)))
feedback_n_li.insert(beck_feed3)


feedback_q_siz1 = {
    "1) Mentor o'z vaqtida ish joyida yo'q": "Mentor o'z vaqtida ish joyida yo'q",
    "2) Mentor umuman yordam bera olmadi": "Mentor umuman yordam bera olmadi",
    "3) Mentor yordam berishdan bosh tortdi": "Mentor yordam berishdan bosh tortdi"
}
feedback_q_siz = InlineKeyboardMarkup(row_width=1)
for k, v in feedback_q_siz1.items():
    feedback_q_siz.insert(InlineKeyboardButton(text=k,  callback_data=feed3.new(item_feed=v)))
feedback_q_siz.insert(beck_feed3)




