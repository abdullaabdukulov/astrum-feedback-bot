from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from admin.handlers.others import all_mentor_full_name, all_admin_full_name, all_view_full_name, \
    all_ds, all_fs, all_se

mentors_add_inl = InlineKeyboardMarkup(row_width=3).add(
    InlineKeyboardButton(text='Data Science', callback_data='DS'),
    InlineKeyboardButton(text='Full Stack', callback_data='FS'),
    InlineKeyboardButton(text='Software Engineering', callback_data='SE'),
)


def all_ment():
    mentors_delete_inl = InlineKeyboardMarkup(row_width=1)
    for a in all_mentor_full_name():
        mentors_delete_inl.add(InlineKeyboardButton(text=a, callback_data=a))
    return mentors_delete_inl.add(InlineKeyboardButton(text="🔙 Ortga", callback_data="delete_back_mentor"))


def all_admin():
    admin_delete_inl = InlineKeyboardMarkup(row_width=1)
    for i in all_admin_full_name():
        if i != 'unique_admin':
            admin_delete_inl.add(InlineKeyboardButton(text=i, callback_data=i))
    return admin_delete_inl.add(InlineKeyboardButton(text="🔙 Ortga", callback_data="delete_back_admin"))


def all_access():
    admin_view_inl = InlineKeyboardMarkup(row_width=1)
    for i in all_view_full_name():
        admin_view_inl.add(InlineKeyboardButton(text=i, callback_data=i))
    return admin_view_inl.add(InlineKeyboardButton(text="🔙 Ortga", callback_data="delete_back_admin"))


analysis_direction = InlineKeyboardMarkup(row_width=3).add(
    InlineKeyboardButton(text='Data Science', callback_data='data'),
    InlineKeyboardButton(text='Full Stack', callback_data='full'),
    InlineKeyboardButton(text='Software Engineering', callback_data='soft'),
    InlineKeyboardButton(text='umumiy analitika', callback_data='umumiy'),
    InlineKeyboardButton(text='Web saytda kirish', url='http://172.20.16.8:8505/'),
    InlineKeyboardButton(text='🔙 Ortga', callback_data='main_kirish')
)

umumiy_analysis_inl = InlineKeyboardMarkup(row_width=2).add(
    InlineKeyboardButton(text='Umumiy yo\'nalish', callback_data='umummiy_direction'),
    InlineKeyboardButton(text='Umumiy mentor', callback_data='umumiy_metors'),
    InlineKeyboardButton(text='🔙 Ortga' ,callback_data='ortga')
)

mentors_umummiy_inl = InlineKeyboardMarkup(row_width=3).add(
    InlineKeyboardButton(text='Data Science', callback_data='Data Science'),
    InlineKeyboardButton(text='Full Stack', callback_data='Full Stack'),
    InlineKeyboardButton(text='Software Engineering', callback_data='Software Engineering'),
    InlineKeyboardButton(text='🔙 Ortga' ,callback_data='orqaga'),
)



def all_ds_inline():
    all_ds_mentors = InlineKeyboardMarkup(row_width=1)
    for i in all_ds():
        all_ds_mentors.add(InlineKeyboardButton(text=i, callback_data=i+'i'))
    return all_ds_mentors.add(InlineKeyboardButton(text="🔙 Ortga", callback_data='ortga'))


def all_ds_list():
    result = []
    for i in all_ds():
        result.append(i+'i')
    return result


def all_fs_inline():
    all_fs_mentors = InlineKeyboardMarkup(row_width=1)
    for i in all_fs():
        all_fs_mentors.add(InlineKeyboardButton(text=i, callback_data=i+'i'))
    return all_fs_mentors.add(InlineKeyboardButton(text="🔙 Ortga", callback_data='ortga'))


def all_fs_list():
    result = []
    for i in all_fs():
        result.append(i+'i')
    return result


def all_se_inline():
    all_se_mentors = InlineKeyboardMarkup(row_width=1)
    for i in all_se():
        all_se_mentors.add(InlineKeyboardButton(text=i, callback_data=i+'i'))
    return all_se_mentors.add(InlineKeyboardButton(text="🔙 Ortga", callback_data='ortga'))


def all_se_list():
    result = []
    for i in all_se():
        result.append(i+'i')
    return result