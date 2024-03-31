import sqlite3
import json
data = []


def add_data(table_name):
    con = sqlite3.connect('db01.db')
    cur = con.cursor()
    cur.execute(f"SELECT * FROM {table_name}")
    rows = cur.fetchall()
    columns = [column[0] for column in cur.description]
    data1 = []
    for row in rows:
        data1.append(dict(zip(columns, row)))
    con.close()
    return data1


data.append(add_data("users"))
data.append(add_data("professions"))
data.append(add_data("user_profession"))
with open('workers.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

