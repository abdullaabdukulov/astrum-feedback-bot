import sqlite3
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


db_file = f"{BASE_DIR}/data/user.db"
row_path = f"{BASE_DIR}/data/save_row.json"


def mentors_datas():
    from sqlite3 import connect
    conn = connect(db_file)
    curr = conn.cursor()
    data = curr.execute("""
                    SELECT full_name, directions FROM mentors;
                    """)
    result = []
    for row in data.fetchall():
        result.append(row)
    curr.close()
    return result


def users_data():
    from sqlite3 import connect
    conn = connect(db_file)
    curr = conn.cursor()
    data = curr.execute("""
                    SELECT user_id, directions, last_feedback FROM users;
                    """)
    result = []
    for row in data.fetchall():
        result.append(row)
    curr.close()
    return result


def users_add(user_id, direction, last_feedback):
    from sqlite3 import connect
    conn = connect(db_file)
    curr = conn.cursor()
    curr.execute("INSERT INTO users values(?,?,?)", (user_id, direction, last_feedback))
    conn.commit()
    curr.close()


def update_last_feedback(user_id, date):
    sqlite_connection = sqlite3.connect(db_file)
    curr = sqlite_connection.cursor()
    query = """UPDATE users SET last_feedback = ? WHERE user_id = ?"""
    curr.execute(query, (date, user_id))
    sqlite_connection.commit()
    curr.close()


def save_row(row):
    with open(row_path, 'w') as f:
        json.dump(row, f)
        f.close()


def update_direction(user_id, directions):
    conn = sqlite3.connect(db_file)
    curr = conn.cursor()
    query = """UPDATE users SET directions = ? WHERE user_id = ?"""
    curr.execute(query, (directions, user_id,))
    conn.commit()
    curr.close()

