from datetime import datetime
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from data.google_sheet import google_sheet_add
from data.query_data import update_last_feedback, users_add, users_data, update_direction
from keyboards.default.menu_keyboard import menu
from keyboards.inline.student_parts import mentors_data, mentors_full, mentors_soft, feedback_de3, yonalish, \
    feedback_q_li, feedback_n_li, feedback_q_siz

from loader import dp
from states.student_part_state import Student_part_state


r_id = 0


def all_user_id():
    return [i[0] for i in users_data()]


def all_user_der():
    return [i[1] for i in users_data()]


def last_feed_back_user():
    return [i[2] for i in users_data()]


# print(last_feed_back_user()[all_user_id().index(784286636)])

##################     back     ##################
@dp.callback_query_handler(text="back_menu", state=[Student_part_state.yonalishlar, Student_part_state.mentorlar, Student_part_state.chenged])
async def back_menu(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Menu", reply_markup=menu)
    await call.message.delete()
    await call.answer(cache_time=60)
    await state.finish()


@dp.callback_query_handler(text="back_mentor", state=Student_part_state.feed3)
async def back_der(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=60)
    w = await state.get_data()
    m = w['mentor'].split(':')[0]
    all_mentor = [mentors_data(), mentors_full(), mentors_soft()]
    all_mentor_link = ["DS", "FS", "SE"]
    idx = all_mentor_link.index(m)
    await call.message.edit_reply_markup(reply_markup=all_mentor[idx])
    await Student_part_state.mentorlar.set()


@dp.callback_query_handler(text="back_feed3", state=Student_part_state.sabab)
async def back(call: CallbackQuery, state: FSMContext):
    await call.message.edit_reply_markup(reply_markup=feedback_de3)
    await call.answer(cache_time=60)
    await Student_part_state.feed3.set()


#################### direction changed ######################

@dp.message_handler(text="/direction")
async def dir_get(msg: Message):
    await msg.answer("Iltimos o'z yo'nalishingizni tanlang", reply_markup=yonalish)
    await Student_part_state.chenged.set()


@dp.callback_query_handler(state=Student_part_state.chenged)
async def dir_chenged(call : CallbackQuery, state : FSMContext):
    await call.answer(cache_time=60)
    await call.message.delete()
    direction, id = call.data, call.from_user.id
    # print(direction, id)
    update_direction(id, direction)
    await state.finish()
    await call.message.answer("Yo'nalishingiz muffaqqiyatli o'zgartirlidi")
    await call.message.answer("Menu", reply_markup=menu)


##############################Mentors_aprt######################################################
@dp.message_handler(text="Mentorga feedback qoldirish")
async def student_part(msg: Message):
    userid = msg.from_user.id + r_id
    der = ""
    try:
        der = all_user_der()[all_user_id().index(userid)]
    except:
        pass

    if userid not in all_user_id():
        await msg.answer("Iltimos o'z yo'nalishingizni tanlang", reply_markup=yonalish)
        await Student_part_state.yonalishlar.set()

    else:
        if der == "DS":
            await msg.answer("Data Science Mentorlari", reply_markup=mentors_data())
            await Student_part_state.mentorlar.set()

        elif der == "FS":
            await msg.answer("Data Science Mentorlari", reply_markup=mentors_full())
            await Student_part_state.mentorlar.set()

        elif der == "SE":
            await msg.answer("Data Science Mentorlari", reply_markup=mentors_soft())
            await Student_part_state.mentorlar.set()


##################data_science####################
@dp.callback_query_handler(text="DS", state=Student_part_state.yonalishlar)
async def data_science(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Qaysi mentorga feedback qoldirmochisiz ?", reply_markup=mentors_data())
    await call.answer(cache_time=60)
    der = call.data
    await state.update_data(der=der)
    await call.message.delete()
    await Student_part_state.next()


################## full stack ################################
@dp.callback_query_handler(text="FS", state=Student_part_state.yonalishlar)
async def full_stack(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Qaysi mentorga izoh qoldirmochisiz ?", reply_markup=mentors_full())
    await call.answer(cache_time=60)
    der = call.data
    await state.update_data(der=der)
    await call.message.delete()
    await Student_part_state.next()


################## softwere ################################
@dp.callback_query_handler(text="SE", state=Student_part_state.yonalishlar)
async def softwer(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Qaysi mentorga izoh qoldirmochisiz ?", reply_markup=mentors_soft())
    await call.answer(cache_time=60)
    der = call.data
    await state.update_data(der=der)
    await call.message.delete()
    await Student_part_state.next()


# pop = ["komiljon_x","asal_a","nodira_q","abdulaziz_w","aziza_a","rahmatulloh_r","jasur_sh","sarvarbek_sh","ali_m","vali_m","uqw_q"]

################# feedback part ##########################

@dp.callback_query_handler(state=Student_part_state.mentorlar)
async def feedback(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Feedback tanlang", reply_markup=feedback_de3)
    await call.answer(cache_time=60)
    m = call.data
    await state.update_data(mentor=m)
    await call.message.delete()
    await Student_part_state.next()


@dp.callback_query_handler(text="Qoniqarli", state=Student_part_state.feed3)
async def feedbac2(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Nima sabab ?", reply_markup=feedback_q_li)
    m = call.data
    await state.update_data(feedback=m)
    await call.message.delete()
    await Student_part_state.next()


@dp.callback_query_handler(text="Namunali", state=Student_part_state.feed3)
async def feedbac3(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Nima sabab ?", reply_markup=feedback_n_li)
    m = call.data
    await state.update_data(feedback=m)
    await call.message.delete()
    await Student_part_state.next()


@dp.callback_query_handler(text="Qoniqarsiz", state=Student_part_state.feed3)
async def feedbac4(call: CallbackQuery, state: FSMContext):
    await call.message.answer("Nima sabab ?", reply_markup=feedback_q_siz)
    m = call.data
    await state.update_data(feedback=m)
    await call.message.delete()
    await Student_part_state.next()


@dp.callback_query_handler(state=Student_part_state.sabab)
async def feedbac_end(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    userid1 = call.from_user.id + r_id
    hour, minut = 0, 0
    try:
        date = last_feed_back_user()[all_user_id().index(userid1)]
        date_1 = datetime.strptime(date, '%Y-%m-%d %H:%M')
        date2 = datetime.now().strftime("%Y-%m-%d %H:%M")
        date_now = datetime.strptime(date2, "%Y-%m-%d %H:%M")
        min = date_now - date_1

        if len(str(min)) <= 7:
            hour = int(str(min).split(":")[0])
            minut = int(str(min).split(":")[1])
        else:
            hour = 2

    except:
        hour = 2

    if hour >= 2:
        await call.answer("Siz bergan feedback qabul qilindi.", cache_time=60, show_alert=True)
        end = call.data
        await state.update_data(end=end)
        db = await state.get_data()

        we, balls = ['q_li', "n_li", 'q_siz'], [1, 2, -1]
        ball = balls[we.index(db['end'].split(':')[0])]

        data_for_sheet = [db['mentor'].split(":")[0], db['mentor'].split(':')[1], db['feedback'], db['end'].split(':')[1], ball]
        google_sheet_add(data_for_sheet)

        await call.message.answer(
            "Qoldirgan feedbackingiz uchun rahmat.", reply_markup=menu)

        if userid1 not in all_user_id():
            date = datetime.now().strftime("%Y-%m-%d %H:%M")
            users_add(userid1, db['der'], date)

        else:
            date2 = datetime.now().strftime("%Y-%m-%d %H:%M")
            update_last_feedback(userid1, date2)

    else:
        await call.answer("✖️ Siz har 2 soatda bir marta feedback bera olasiz", cache_time=60, show_alert=True)
        await call.message.answer(f"Siz {hour}:{minut} minut oldin feedback berdingiz", reply_markup=menu)

    await state.finish()