import sqlite3
from datetime import datetime


# conn = sqlite3.connect('../user.db')
# curr = conn.cursor()
# result = [(1, 'Data Science')]
# curr.execute("""CREATE TABLE IF NOT EXISTS mentors(mentor_id INTEGER, full_name STRING NOT NULL, directions STRING NOT NULL);""")
# curr.execute("""CREATE TABLE IF NOT EXISTS users(user_id INTEGER NOT NULL primary key UNIQUE, directions STRING NOT NULL, last_feedback TEXT)""")
# for a in result:
# curr.execute(f"INSERT INTO users VALUES(?,?, {strftime('%Y-%m-%d %H:%M:%S', gmtime())}", a)
# conn.commit()

# curr.execute("""CREATE TABLE IF NOT EXISTS admins(id INTEGER NOT NULL PRIMARY KEY UNIQUE, full_name TEXT NOT NULL UNIQUE)""")
# curr.close()
# print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# curr.execute(f"INSERT INTO admins VALUES(?,?)", (2143798298, 'Abdulla Abduqulov'))
# conn.commit()
# conn.close()

abl_path = '/Users/student/Desktop/bot/My_Mentor_feedback_bot/data/user.db'


def check_admin(number):
    import sqlite3
    with sqlite3.connect(abl_path) as db:
        cursor = db.cursor()
        check = cursor.execute(f"SELECT EXISTS(SELECT 1 FROM admins WHERE id={number})").fetchone()[0]
        cursor.close()
    return check


def check_analysis_users(number):
    conn = sqlite3.connect(abl_path)
    curr = conn.cursor()
    check = curr.execute(f"SELECT EXISTS(SELECT 1 FROM user_access WHERE user_id={number})").fetchone()[0]
    curr.close()
    return check
# print(check_admin(2))


def add_mentor_query(data):
    import sqlite3
    conn = sqlite3.connect(abl_path)
    curr = conn.cursor()
    curr.execute("INSERT OR IGNORE INTO mentors(full_name, directions) VALUES(?, ?)",
                 (data['full_name'], data['direction']))
    conn.commit()
    curr.close()


# print(add_mentor_query({'full_name': 'Komiljon', 'direction': 'Data Science'}))


def mentor_delete_query(name):
    sqlite_connection = sqlite3.connect(abl_path)
    cursor = sqlite_connection.cursor()
    print("Подключен к SQLite")

    sql_delete_query = """DELETE from mentors where full_name = ?"""
    cursor.execute(sql_delete_query, (name,))
    sqlite_connection.commit()
    print("Запись успешно удалена")
    cursor.close()


def all_mentor_full_name():
    sqlite_connection = sqlite3.connect(abl_path)
    cursor = sqlite_connection.cursor()
    query = """SELECT full_name from mentors"""
    query_set = cursor.execute(query)
    all_data = []
    for row in query_set.fetchall():
        all_data.append(row[0])
    cursor.close()
    return all_data


# def all_mentor_full_data():
#     sqlite_connection = sqlite3.connect('/Users/student/telegram_bots/user.db')
#     cursor = sqlite_connection.cursor()
#     query = """SELECT full_name, directions from mentors"""
#     query_set = cursor.execute(query)
#     all_data = []
#     for row in query_set.fetchall():
#         all_data.append(row)
#     cursor.close()
#     return all_data


# print(all_mentor_full_data())

# mentor_delete_query('Komiljon')
# mentor_delete_query()


# def mentor_edit_query(new_name, name, directions):
#     conn = sqlite3.connect('/Users/student/telegram_bots/user.db')
#     curr = conn.cursor()
#     curr.execute("UPDATE mentors SET full_name=%s, directions=%s WHERE like full_name="%?%" % (new_name, directions), (name,))
#     conn.commit()
#     print('Successfully')
#     curr.close()


# mentor_edit_query('Abdulla', 'Abdulla Abduqulov', 'DsS')


def get_users():
    conn = sqlite3.connect(abl_path)
    cursor = conn.cursor()
    queryset = cursor.execute("""SELECT user_id FROM users""")
    result = []
    for a in queryset.fetchall():
        result.append(a)
    return result
# get_users()

def add_admin(data):
    conn = sqlite3.connect(abl_path)
    curr = conn.cursor()
    curr.execute("INSERT OR IGNORE INTO admins(id, full_name) VALUES(?, ?)",
                 (data['admin_id'], data['fullname']))
    conn.commit()
    curr.close()


def delete_admin(name):
    sqlite_connection = sqlite3.connect(abl_path)
    cursor = sqlite_connection.cursor()
    # print("Подключен к SQLite")
    sql_delete_query = """DELETE from admins where full_name = ?"""
    cursor.execute(sql_delete_query, (name,))
    sqlite_connection.commit()
    # print("Запись успешно удалена")
    cursor.close()


def all_admin_full_name():
    sqlite_connection = sqlite3.connect(abl_path)
    cursor = sqlite_connection.cursor()
    query = """SELECT full_name from admins"""
    query_set = cursor.execute(query)
    all_data = []
    for row in query_set.fetchall():
        all_data.append(row[0])
    cursor.close()
    return all_data


import json


def add_user_access(data):
    conn = sqlite3.connect(abl_path)
    curr = conn.cursor()
    curr.execute("INSERT OR IGNORE INTO user_access(user_id, full_name) VALUES(?, ?)",
                 (data['admin_id'], data['fullname']))
    conn.commit()
    curr.close()


def edit_password(password):
    with open('/Users/student/Desktop/bot/My_Mentor_feedback_bot/data/password.json', 'w') as f:
        json.dump(password, f)
        f.close()


def delete_user_access(name):
    sqlite_connection = sqlite3.connect(abl_path)
    cursor = sqlite_connection.cursor()
    # print("Подключен к SQLite")
    sql_delete_query = """DELETE from user_access where full_name = ?"""
    cursor.execute(sql_delete_query, (name,))
    sqlite_connection.commit()
    # print("Запись успешно удалена")
    cursor.close()


def all_view_full_name():
    conne = sqlite3.connect(abl_path)
    cursor = conne.cursor()
    query = """SELECT full_name from user_access"""
    query_set = cursor.execute(query)
    all_data = []
    for row in query_set.fetchall():
        all_data.append(row[0])
    cursor.close()
    return all_data


def all_ds():
    conn = sqlite3.connect(abl_path)
    cur = conn.cursor()
    all_ = cur.execute("""SELECT full_name FROM mentors WHERE directions='DS'""")
    result = []
    for a in all_.fetchall():
        result.append(a[0])
    return result


def all_fs():
    conn = sqlite3.connect(abl_path)
    cur = conn.cursor()
    all_ = cur.execute("""SELECT full_name FROM mentors WHERE directions='FS'""")
    result = []
    for a in all_.fetchall():
        result.append(a[0])
    return result


def all_se():
    conn = sqlite3.connect(abl_path)
    cur = conn.cursor()
    all_ = cur.execute("""SELECT full_name FROM mentors WHERE directions='SE'""")
    result = []
    for a in all_.fetchall():
        result.append(a[0])
    return result

# edit_password('student#2022')

# with open('/Users/student/telegram_bots/password.json', 'r') as f:
#     s = json.load(f)
#     f.close()
# print(s)


# conn = sqlite3.connect('/Users/student/telegram_bots/user.db')
# curr = conn.cursor()
# curr.execute("""CREATE TABLE IF NOT EXISTS user_access(user_id INTEGER NOT NULL PRIMARY KEY UNIQUE, full_name TEXT NOT NULL UNIQUE)""")
# conn.commit()
# curr.close()