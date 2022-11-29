import time
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher

from admin.analysis.vizual_part import umumit_analitika, data_science_analitika, full_stack_analitika, mentors_analysis, \
    soft_engineer_analitika
from admin.handlers import others
from admin.handlers.others import add_mentor_query, mentor_delete_query, get_users, add_admin, delete_admin, \
    edit_password, add_user_access, check_analysis_users, delete_user_access
from admin.keyboards import admin_kb, inlines
from admin.keyboards.admin_kb import main_kb, edit_password_kb, main_analysis, access_user_kb, view_analysis_kb
from admin.keyboards.inlines import all_ds_inline, all_fs_inline, all_fs_list, all_se_inline, all_se_list, \
    analysis_direction, umumiy_analysis_inl, mentors_umummiy_inl
from keyboards.default.menu_keyboard import menu
from loader import dp, bot
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent  # /Users/student/web_scraping/astrum-feedback-bot


###### ADMIN ##########

@dp.message_handler(commands=['admin'])
async def admin_main(message: types.Message):
    if others.check_admin(message.from_user.id):
        await message.answer(f'Admin Panelga Xush kelibsiz!', reply_markup=admin_kb.main_kb)

#########MENTOR TAHRIRLASH############
@dp.message_handler(text='Mentor tahrirlash')
async def edit_mentor(message: types.Message):
    if others.check_admin(message.from_user.id):
        await message.answer('Mentor tahrirlash', reply_markup=admin_kb.edit_mentor_kb)

################# MENTOR QOSHISH#####################

class FSMAdmin(StatesGroup):
    fullname = State()
    direction = State()


@dp.message_handler(text="qo'shish")
async def mentor_add_name_part_1(message: types.Message):
    if others.check_admin(message.from_user.id):
        await message.answer("Mentorning toliq ismi va familyasini kiriting.")
        await FSMAdmin.fullname.set()


@dp.message_handler(state=FSMAdmin.fullname)
async def mentor_add_name_part_2(message: types.Message, state: FSMContext):
    if others.check_admin(message.from_user.id):
        await message.answer("Mentor yo'nalishini tanlang.", reply_markup=inlines.mentors_add_inl)
        name = message.text
        await state.update_data(full_name=name)
        await FSMAdmin.next()


@dp.callback_query_handler(text=['DS', 'FS', 'SE'], state=FSMAdmin.direction)
async def mentor_add_name_part_3(call: types.CallbackQuery, state: FSMContext):
    direction = call.data
    await state.update_data(direction=direction)
    db = await state.get_data()
    await state.finish()
    add_mentor_query(db)
    # call.data.delete()
    await call.message.delete()
    await call.message.answer(text='Muvoffaqiyatli bajarildi.', reply_markup=main_kb)


################MENTOR OCHIRISH#####################

class FSMDelete(StatesGroup):
    fullname = State()


@dp.callback_query_handler(text='delete_back_admin', state=FSMDelete.fullname)
async def back_delete_mentor(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer('🔙 Ortga', reply_markup=admin_kb.edit_mentor_kb)
    await callback.answer(cache_time=60)
    await request_message.delete()
    await state.finish()


@dp.message_handler(text="o'chirish")
async def mentor_delete_part_1(message: types.Message):
    if others.check_admin(message.from_user.id):
        if len(inlines.all_ment()['inline_keyboard']) > 0:
            # print(inlines.all_ment()['inline_keyboard'] is True)
            await message.answer(text='Qaysi mentorni o\'chirmoqchisiz?', reply_markup=inlines.all_ment())
            await FSMDelete.fullname.set()
        else:
            await message.answer('Mentorlar yo\'q', reply_markup=main_kb)


@dp.callback_query_handler(state=FSMDelete.fullname)
async def mentor_delete_part_2(callback: types.callback_query, state=FSMContext):
    name = callback.data
    await state.update_data(fullname=name)
    db = await state.get_data()
    await state.finish()
    mentor_delete_query(db['fullname'])
    await callback.message.delete()
    await callback.message.answer(text='Muvoffaqiyatli bajarildi.', reply_markup=main_kb)

##############ELON##############


class FMSElon(StatesGroup):
    text = State()


@dp.message_handler(text="E'lon")
async def elon_part_1(message: types.Message):
    if others.check_admin(message.from_user.id):
        await message.answer('Foydalanuvchilarga e\'loningizni yozing.')
        await FMSElon.text.set()


@dp.message_handler(state=FMSElon.text)
async def elon_part_2(message: types.Message, state=FSMContext):
    global loading
    text = message.text
    await state.update_data(reklama=text)
    db = await state.get_data()
    await state.finish()
    try:
        loading = await message.answer('Jo\'natilmoqda...')
        for a in get_users():
            await bot.send_message(a, text=db['reklama'])
            time.sleep(1)
    except:
        print('Xatolik elon partda')
    await loading.delete()
    await message.answer(text='Muvofaqqiyatli bajarildi.', reply_markup=main_kb)

#################ADMIN QOSHISH###################

class FSMAdmin_add(StatesGroup):
    fullname = State()
    admin_id = State()


@dp.message_handler(text='Admin tahrirlash')
async def add_admin_part_1(message: types.Message):
    if others.check_admin(message.from_user.id):
        await message.answer('Admin tahrirlash', reply_markup=admin_kb.edit_admin_kb)


@dp.message_handler(text="admin qo'shish")
async def add_admin_part_2(message: types.Message):
    if others.check_admin(message.from_user.id):
        await message.answer('Yangi adminnig ismini kiriting.')
        await FSMAdmin_add.fullname.set()


@dp.message_handler(state=FSMAdmin_add.fullname)
async def add_admin_part_4(message: types.Message, state: FSMContext):
    await message.answer("Yangi adminning 'User_id' sini kiritng.. ")
    name = message.text
    await state.update_data(fullname=name)
    await FSMAdmin_add.next()


@dp.message_handler(state=FSMAdmin_add.admin_id)
async def add_admin_part_5(message: types.Message, state=FSMContext):
    admin_id = message.text
    await state.update_data(admin_id=admin_id)
    db = await state.get_data()
    await state.finish()
    add_admin(db)
    await message.answer(text='Muvoffaqiyatli bajarildi.', reply_markup=main_kb)


################### admin delete ################

class FSMAdmin_delete(StatesGroup):
    fullname = State()


@dp.message_handler(text='admin o\'chirish')
async def admin_delete_part_1(message: types.Message):
    if others.check_admin(message.from_user.id):
        global request_message
        if len(inlines.all_admin()['inline_keyboard']) > 1:
            # print(inlines.all_ment()['inline_keyboard'] is True)
            request_message = await message.answer(text='Qaysi adminni o\'chirmoqchisiz?', reply_markup=inlines.all_admin())
            await FSMUser_access_delete.fullname.set()
        else:
            await message.answer('Sizdan boshqa admin yo\'q', reply_markup=main_kb)


@dp.callback_query_handler(text='delete_back_admin', state=FSMAdmin_delete.fullname)
async def back_delete_admin(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer('🔙 Ortga', reply_markup=admin_kb.edit_admin_kb)
    await callback.answer(cache_time=60)
    await request_message.delete()
    await state.finish()


@dp.callback_query_handler(state=FSMAdmin_delete.fullname)
async def admin_delete_part_2(callback: types.callback_query, state=FSMContext):
    if callback.data != 'delete_back_admin':
        name = callback.data
        await state.update_data(fullname=name)
        db = await state.get_data()
        await state.finish()
        delete_admin(db['fullname'])
        await callback.message.delete()
        await callback.message.answer(text='Muvoffaqiyatli bajarildi.', reply_markup=main_kb)
        await callback.answer(cache_time=60)

############Parolni tahrirlash###############


class FSM_password(StatesGroup):
    password = State()


@dp.message_handler(text='Parol tahrirlash')
async def edit_password_part_1(message: types.Message):
    if others.check_admin(message.from_user.id):
        await message.answer('Parol tahrirlash', reply_markup=edit_password_kb)


@dp.message_handler(text='parolni tahrirlash')
async def edit_password_part_2(message: types.Message):
    await message.answer('Yangi parol kiriting:')
    await FSM_password.password.set()


@dp.message_handler(state=FSM_password.password)
async def edit_password_part_3(message: types.Message, state=FSMContext):
    password = message.text
    await state.update_data(password=password)
    db = await state.get_data()
    await state.finish()
    edit_password(db['password'])
    await message.answer(f"Muvoffaqiyatli bajarildi.\nYangi parol: {db['password']}.", reply_markup=main_kb)


@dp.message_handler(text='🔙 Ortga')
async def back_kb(message: types.Message):
    if others.check_admin(message.from_user.id):
        await message.answer('Bosh Menu', reply_markup=main_kb)

###############Muayyan odamlar qoshish###################



@dp.message_handler(text='Mentorlar analitikasi')
async def analysis_part_1(message: types.Message):
    if others.check_admin(message.from_user.id):
        await message.answer('Mentorlar analitikasi', reply_markup=main_analysis)


@dp.message_handler(text='Analaitikani ko\'rishga dostup berish')
async def view_analysis_part_1(message: types.Message):
    if others.check_admin(message.from_user.id):
        await message.answer('Analaitikani ko\'rishga dostup berish', reply_markup=access_user_kb)

#############################ADDD  STATE############################################################


class FSMUser_access_add(StatesGroup):
    fullname = State()
    admin_id = State()


@dp.message_handler(text='ruxsat qo\'shish')
async def view_analysis_part_1(message: types.Message):
    if others.check_admin(message.from_user.id):
        await message.answer('Yangi analitikadan foydalanuvchining to\'liq ismini kiriting.')
        await FSMUser_access_add.fullname.set()


@dp.message_handler(state=FSMUser_access_add.fullname)
async def view_analysis_part_2(message: types.Message, state: FSMContext):
    await message.answer("Yangi analitikadan foydalanuvchining 'User_id' sini kiritng.. ")
    name = message.text
    await state.update_data(fullname=name)
    await FSMUser_access_add.next()


@dp.message_handler(state=FSMUser_access_add.admin_id)
async def view_analysis_part_3(message: types.Message, state=FSMContext):
    admin_id = message.text
    await state.update_data(admin_id=admin_id)
    db = await state.get_data()
    print(db)
    await state.finish()
    add_user_access(db)
    await message.answer(text='Muvoffaqiyatli bajarildi.', reply_markup=main_kb)


@dp.message_handler(text='🔙 Ortga.')
async def del_back_kb(message: types.Message):
    if others.check_admin(message.from_user.id):
        await message.answer('Bosh Menu', reply_markup=main_analysis)
    elif check_analysis_users(message.from_user.id):
        await message.answer('Bosh menu', reply_markup=menu)


########################DELETE STATE#############################################################


class FSMUser_access_delete(StatesGroup):
    fullname = State()


@dp.message_handler(text='ruxsatni o\'chirish')
async def delete_access_part_1(message: types.Message):
    if others.check_admin(message.from_user.id):
        global request_message
        if len(inlines.all_access()['inline_keyboard']) > 1:
            # print(inlines.all_ment()['inline_keyboard'] is True)
            request_message = await message.answer(text='Qaysi ko\'ruvchilarni o\'chirmoqchisiz?', reply_markup=inlines.all_access())
            await FSMUser_access_delete.fullname.set()
        else:
            await message.answer('Sizdan boshqa ko\'ruvchilarni yo\'q', reply_markup=main_kb)


@dp.callback_query_handler(text='delete_access_back', state=FSMUser_access_delete.fullname)
async def delete_access_part_2(callback: types.CallbackQuery, state: FSMContext):
    if others.check_admin(callback.message.from_user.id):
        await callback.message.answer('🔙 Ortga', reply_markup=admin_kb.access_user_kb)
        await callback.answer(cache_time=60)
        await request_message.delete()
        await state.finish()


@dp.callback_query_handler(state=FSMUser_access_delete.fullname)
async def delete_access_part_3(callback: types.callback_query, state=FSMContext):
    name = callback.data
    await state.update_data(fullname=name)
    db = await state.get_data()
    await state.finish()
    delete_user_access(db['fullname'])
    await callback.message.delete()
    await callback.message.answer(text='Muvoffaqiyatli bajarildi.', reply_markup=main_kb)
    await callback.answer(cache_time=60)


@dp.message_handler(text='🔝 Asosiy Menyu')
async def asososiy_menu(message: types.Message):
   await message.answer('🔝 Asosiy Menyu', reply_markup=menu)


###############Analitikani ko'rish###############

@dp.message_handler(text=['Analitikani ko\'rish'])
async def analysis_view_part_1(message: types.Message):
    if check_analysis_users(message.from_user.id) or others.check_admin(message.from_user.id):
        # await message.answer('yangilanmoqda...')
        # await message.delete()
        await message.answer('Analitikani ko\'rish', reply_markup=view_analysis_kb)


# @dp.message_handler(text='Haftalik')
# async def analysis_view_part_2(message: types.Message):
#     await message.answer('rasm va link')


@dp.message_handler(text='Kirish')
async def analysis_view_part_2(message: types.Message):
    if check_analysis_users(message.from_user.id) or others.check_admin(message.from_user.id):
        await message.answer('Qaysi yonalish?', reply_markup=analysis_direction)
        umumit_analitika() ## update data for visualization

######### directions ############

######## data science#############

@dp.callback_query_handler(text='data')
async def analysis_view_part_3(call: types.CallbackQuery):
    # if check_analysis_users(call.message.from_user.id) or others.check_admin(call.message.from_user.id):
    await call.message.delete()
    await call.message.answer('Mentorlar analitikasi', reply_markup=all_ds_inline())


@dp.callback_query_handler(text=all_ds_list())
async def send_visual_ds(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('kuting!')
    data_science_analitika(call.data[:-1])
    photo1 = f'/Users/student/Desktop/bot/My_Mentor_feedback_bot/data/visual/directions/data_science/{call.data[:-1]}_1.png'
    photo2 = f'/Users/student/Desktop/bot/My_Mentor_feedback_bot/data/visual/directions/data_science/{call.data[:-1]}_2.png'
    # print(call.message.text)
    p1 = open(photo1, 'rb')
    p2 = open(photo2, 'rb')
    await bot.send_photo(call.from_user.id, photo=p1)
    await bot.send_photo(call.from_user.id, photo=p2)
    await call.message.answer('Muvoffaqiyatli bajarildi!', reply_markup=view_analysis_kb)

###############full stack #######################

@dp.callback_query_handler(text='full')
async def analysis_view_part_4(call: types.CallbackQuery):
    # if check_analysis_users(call.message.from_user.id) or others.check_admin(call.message.from_user.id):
    await call.message.delete()
    await call.message.answer('Mentorlar analitikasi', reply_markup=all_fs_inline())


@dp.callback_query_handler(text=all_fs_list())
async def send_visual_fs(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('kuting!')
    full_stack_analitika(call.data[:-1])
    photo1 = f'{BASE_DIR}/data/visual/directions/full_stack/{call.data[:-1]}_1.png'
    photo2 = f'{BASE_DIR}/data/visual/directions/full_stack/{call.data[:-1]}_2.png'
    # print(call.message.text)
    p1 = open(photo1, 'rb')
    p2 = open(photo2, 'rb')
    await bot.send_photo(call.from_user.id, photo=p1)
    await bot.send_photo(call.from_user.id, photo=p2)
    await call.message.answer('Muvoffaqiyatli bajarildi!', reply_markup=view_analysis_kb)

############### software enineering $$$$$$$$$$$$$$$$$

@dp.callback_query_handler(text='soft')
async def analysis_view_part_5(call: types.CallbackQuery):
    # if check_analysis_users(call.message.from_user.id) or others.check_admin(call.message.from_user.id):
    await call.message.delete()
    await call.message.answer('Mentorlar analitikasi', reply_markup=all_se_inline())


@dp.callback_query_handler(text=all_se_list())
async def send_visual_se(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('kuting!')
    soft_engineer_analitika(call.data[:-1])
    photo1 = f'{BASE_DIR}/data/visual/directions/software/{call.data[:-1]}_1.png'
    photo2 = f'{BASE_DIR}/visual/directions/software/{call.data[:-1]}_2.png'
    # print(call.message.text)
    p1 = open(photo1, 'rb')
    p2 = open(photo2, 'rb')
    await bot.send_photo(call.from_user.id, photo=p1)
    await bot.send_photo(call.from_user.id, photo=p2)
    await call.message.answer('Muvoffaqiyatli bajarildi!', reply_markup=view_analysis_kb)

@dp.message_handler(commands=['analysis'])
async def dopstup_ochish(message: types.Message):
    if check_analysis_users(message.from_user.id) or others.check_admin(message.from_user.id):
        await message.answer('Analitikani ko\'rish', reply_markup=view_analysis_kb)


@dp.callback_query_handler(text='main_kirish')
async def back_to_kirish(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('🔙 Ortga', reply_markup=view_analysis_kb)

@dp.callback_query_handler(text='ortga')
async def back_to_mentors(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('🔙 Ortga', reply_markup=analysis_direction)

#############umumiy analitikia""""""""
@dp.callback_query_handler(text='umumiy')
async def umumiy_ananitika(call: types.callback_query):
    await call.message.delete()
    await call.message.answer('Qaysi kategoriya', reply_markup=umumiy_analysis_inl)

##########umumiy yonalish ###############
@dp.callback_query_handler(text='umummiy_direction')
async def umumiy_yonalish(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('kuting!')
    umumit_analitika()
    photo1 = f'{BASE_DIR}/data/visual/umumiy/yonalish/all.png'
    photo2 = f'{BASE_DIR}/data/visual/umumiy/yonalish/all2.png'
    p1 = open(photo1, 'rb')
    p2 = open(photo2, 'rb')
    await bot.send_photo(call.from_user.id, photo=p1)
    await bot.send_photo(call.from_user.id, photo=p2)
    await call.message.answer('Muvoffaqiyatli bajarildi!', reply_markup=view_analysis_kb)


######### umumiy mentor #####################

@dp.callback_query_handler(text='umumiy_metors')
async def umumiy_mentor_part_1(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('Qaysi yo\'nalish', reply_markup=mentors_umummiy_inl)

@dp.callback_query_handler(text=['Data Science', 'Full Stack', 'Software Engineering'])
async def umumiy_mentor_part_2(call: types.CallbackQuery):
    yonalish = call.data
    await call.message.delete()
    await call.message.answer('Kuting..')
    mentors_analysis(yonalish)
    photo1 = f'{BASE_DIR}/data/visual/umumiy/mentor/{yonalish}.png'
    photo2 = f'{BASE_DIR}/data/visual/umumiy/mentor/{yonalish}_1.png'
    p1 = open(photo1, 'rb')
    p2 = open(photo2, 'rb')
    await bot.send_photo(call.from_user.id, photo=p1)
    await bot.send_photo(call.from_user.id, photo=p2)
    await call.message.answer('Muvoffaqiyatli bajarildi!', reply_markup=view_analysis_kb)


@dp.callback_query_handler(text='orqaga')
async def ortga_umumiy_mentor(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('🔙 Ortga', reply_markup=umumiy_analysis_inl)
######## register dispetcher ##################

def register_handler_admin(db: Dispatcher):
    dp.message_handler(admin_main, commands=['admin'])
    dp.message_handler(edit_mentor, text=['Mentor tahrirlash'])