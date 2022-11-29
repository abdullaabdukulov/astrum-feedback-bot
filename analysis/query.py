import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # /Users/student/web_scraping/astrum-feedback-bot

db_file = f"{BASE_DIR}/data/user.db"


def all_mentors():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    data = cursor.execute("""SELECT full_name, directions FROM mentors""")
    result = []
    for i in data.fetchall():
        result.append(i)
    cursor.close()
    result_2 = {"ds_mentors": ['Umumiy analitika'], "se_mentors": ['Umumiy analitika'],
                "fs_mentors": ['Umumiy analitika']}

    for a in result:
        if a[1] == 'DS':
            result_2['ds_mentors'].append(a[0])
        elif a[1] == 'SE':
            result_2['se_mentors'].append(a[0])
        elif a[1] == 'FS':
            result_2['fs_mentors'].append(a[0])

    return result_2

