import sqlite3
from pathlib import Path

from data.config import ADMINS

BASE_DIR = Path(__file__).resolve().parent.parent  # /Users/student/web_scraping/astrum-feedback-bot

db_file = f"{BASE_DIR}/data/user.db"


def create_tables():
    conn = sqlite3.connect(db_file)
    curr = conn.cursor()
    curr.execute(
        """CREATE TABLE IF NOT EXISTS mentors(mentor_id INTEGER, full_name STRING NOT NULL, directions STRING NOT NULL);""")
    curr.execute(
        """CREATE TABLE IF NOT EXISTS users(user_id INTEGER NOT NULL primary key UNIQUE, directions STRING NOT NULL, last_feedback TEXT)""")
    curr.execute(
        """CREATE TABLE IF NOT EXISTS admins(id INTEGER NOT NULL PRIMARY KEY UNIQUE, full_name TEXT NOT NULL UNIQUE)""")
    curr.execute(
        """CREATE TABLE IF NOT EXISTS user_access(user_id INTEGER NOT NULL PRIMARY KEY UNIQUE, full_name TEXT NOT NULL UNIQUE)""")
    conn.commit()
    curr.execute("""INSERT INTO admins values(?,?)""", (int(ADMINS[0]), 'Super Admin'))
    conn.commit()
    curr.close()
    print('successfully database created')


if __name__ == '__main__':
    create_tables()
