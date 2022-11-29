import sqlite3
from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent.parent  # /Users/student/web_scraping/astrum-feedback-bot

db_file = f"{BASE_DIR}/data/user.db"

json_file = f"{BASE_DIR}/data/password.json"


def check_admin(number):
    with sqlite3.connect(db_file) as db:
        cursor = db.cursor()
        check = cursor.execute(f"SELECT EXISTS(SELECT 1 FROM admins WHERE id={number})").fetchone()[0]
        cursor.close()
    return check


def check_analysis_users(number):
    conn = sqlite3.connect(db_file)
    curr = conn.cursor()
    check = curr.execute(f"SELECT EXISTS(SELECT 1 FROM user_access WHERE user_id={number})").fetchone()[0]
    curr.close()
    return check
# print(check_admin(2))


def add_mentor_query(data):
    import sqlite3
    conn = sqlite3.connect(db_file)
    curr = conn.cursor()
    curr.execute("INSERT OR IGNORE INTO mentors(full_name, directions) VALUES(?, ?)",
                 (data['full_name'], data['direction']))
    conn.commit()
    curr.close()


# print(add_mentor_query({'full_name': 'Komiljon', 'direction': 'Data Science'}))


def mentor_delete_query(name):
    sqlite_connection = sqlite3.connect(db_file)
    cursor = sqlite_connection.cursor()
    print("Подключен к SQLite")

    sql_delete_query = """DELETE from mentors where full_name = ?"""
    cursor.execute(sql_delete_query, (name,))
    sqlite_connection.commit()
    print("Запись успешно удалена")
    cursor.close()


def all_mentor_full_name():
    sqlite_connection = sqlite3.connect(db_file)
    cursor = sqlite_connection.cursor()
    query = """SELECT full_name from mentors"""
    query_set = cursor.execute(query)
    all_data = []
    for row in query_set.fetchall():
        all_data.append(row[0])
    cursor.close()
    return all_data


def get_users():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    queryset = cursor.execute("""SELECT user_id FROM users""")
    result = []
    for a in queryset.fetchall():
        result.append(a)
    return result


def add_admin(data):
    conn = sqlite3.connect(db_file)
    curr = conn.cursor()
    curr.execute("INSERT OR IGNORE INTO admins(id, full_name) VALUES(?, ?)",
                 (data['admin_id'], data['fullname']))
    conn.commit()
    curr.close()


def delete_admin(name):
    sqlite_connection = sqlite3.connect(db_file)
    cursor = sqlite_connection.cursor()
    # print("Подключен к SQLite")
    sql_delete_query = """DELETE from admins where full_name = ?"""
    cursor.execute(sql_delete_query, (name,))
    sqlite_connection.commit()
    # print("Запись успешно удалена")
    cursor.close()


def all_admin_full_name():
    sqlite_connection = sqlite3.connect(db_file)
    cursor = sqlite_connection.cursor()
    query = """SELECT full_name from admins"""
    query_set = cursor.execute(query)
    all_data = []
    for row in query_set.fetchall():
        all_data.append(row[0])
    cursor.close()
    return all_data


def add_user_access(data):
    conn = sqlite3.connect(db_file)
    curr = conn.cursor()
    curr.execute("INSERT OR IGNORE INTO user_access(user_id, full_name) VALUES(?, ?)",
                 (data['admin_id'], data['fullname']))
    conn.commit()
    curr.close()


def edit_password(password):
    with open(json_file, 'w') as f:
        json.dump(password, f)
        f.close()


def delete_user_access(name):
    sqlite_connection = sqlite3.connect(db_file)
    cursor = sqlite_connection.cursor()
    # print("Подключен к SQLite")
    sql_delete_query = """DELETE from user_access where full_name = ?"""
    cursor.execute(sql_delete_query, (name,))
    sqlite_connection.commit()
    # print("Запись успешно удалена")
    cursor.close()


def all_view_full_name():
    conne = sqlite3.connect(db_file)
    cursor = conne.cursor()
    query = """SELECT full_name from user_access"""
    query_set = cursor.execute(query)
    all_data = []
    for row in query_set.fetchall():
        all_data.append(row[0])
    cursor.close()
    return all_data


def all_ds():
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    all_ = cur.execute("""SELECT full_name FROM mentors WHERE directions='DS'""")
    result = []
    for a in all_.fetchall():
        result.append(a[0])
    return result


def all_fs():
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    all_ = cur.execute("""SELECT full_name FROM mentors WHERE directions='FS'""")
    result = []
    for a in all_.fetchall():
        result.append(a[0])
    return result


def all_se():
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    all_ = cur.execute("""SELECT full_name FROM mentors WHERE directions='SE'""")
    result = []
    for a in all_.fetchall():
        result.append(a[0])
    return result
