import sqlite3
import json

# conn = connect('../../data/user.db')
# conn.cursor()
# data = conn.execute("""
#                 SELECT full_name, directions FROM mentors;
#                 """)
# conn.close()

absolute_path = '/Users/student/Desktop/bot/My_Mentor_feedback_bot/data/'
db_file = 'user.db'
json_file_row = 'save_row.json'


def mentors_datas():
    from sqlite3 import connect
    conn = connect(absolute_path+db_file)
    curr = conn.cursor()
    data = curr.execute("""
                    SELECT full_name, directions FROM mentors;
                    """)
    result = []
    for row in data.fetchall():
        result.append(row)
    curr.close()
    return result
# print(mentors_data())


def users_data():
    from sqlite3 import connect
    conn = connect(absolute_path+db_file)
    curr = conn.cursor()
    data = curr.execute("""
                    SELECT user_id, directions, last_feedback FROM users;
                    """)
    result = []
    for row in data.fetchall():
        result.append(row)
    curr.close()
    return result

# print(users_data())


def users_add(user_id, direction, last_feedback):
    from sqlite3 import connect
    conn = connect(absolute_path+db_file)
    curr = conn.cursor()
    curr.execute("INSERT INTO users values(?,?,?)", (user_id, direction, last_feedback))
    conn.commit()
    curr.close()


from datetime import datetime

# cursor.execute('''UPDATE books SET price = ? WHERE id = ?''', (newPrice, book_id))
def update_last_feedback(user_id, date):
    sqlite_connection = sqlite3.connect(absolute_path+db_file)
    curr = sqlite_connection.cursor()
    query = """UPDATE users SET last_feedback = ? WHERE user_id = ?"""
    curr.execute(query, (date, user_id))
    sqlite_connection.commit()
    curr.close()

# update_last_feedback(2323232, "qwerfgfhn")
# date = datetime.now().strftime("%d/%m/%y %H:%M")
# users_add(25636523, 'ds', date)


def save_row(row):
    with open('/Users/student/Desktop/bot/My_Mentor_feedback_bot/data/save_row.json', 'w') as f:
        json.dump(row, f)
        f.close()


# edit_password('student#2022')

with open("/Users/student/Desktop/bot/My_Mentor_feedback_bot/data/save_row.json", 'r') as f:
    s = json.load(f)
    f.close()


def update_direction(user_id, directions):
    conn = sqlite3.connect(absolute_path+db_file)
    curr = conn.cursor()
    query = """UPDATE users SET directions = ? WHERE user_id = ?"""
    curr.execute(query, (directions, user_id,))
    conn.commit()
    curr.close()

# update_direction(2143798298, 'DS')
