import sqlite3

con = sqlite3.connect('db01.db')
cur = con.cursor()
cur.execute('DELETE FROM users')
cur.execute('DELETE FROM professions')
cur.execute('DELETE FROM user_profession')
cur.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            phone VARCHAR(11),
            email TEXT,
            created_at TEXT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS professions (
            id INTEGER PRIMARY KEY,
            name TEXT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS user_profession (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            profession_id INTEGER)''')
con.commit()

var_list_users = [
    ("kopanya", "89181111111", "kopanya@kop.kop", "24.03.24"),
    ("chuch", "89182222222", "chuch@ch.ch", "25.03.24"),
    ("ship", "89183333333", "ship@sh.sh", "26.03.24"),
    ("ribb", "89184444444", "ribb@ri.ri", "27.0324")
]
cur.executemany('INSERT INTO users(name, phone, email, created_at) VALUES (?,?,?,?)', var_list_users)
con.commit()
var_list_professions = [
    "programmer",
    "dancer",
    "singer",
    "translator",
    "artist"
]
for i in var_list_professions:
    sql = 'INSERT INTO professions(name) VALUES (?)'
    cur.execute(sql, (i,))
con.commit()
var_list_user_profession =[
    ("kopanya", "programmer"),
    ("kopanya", "dancer"),
    ("kopanya", "singer"),
    ("chuch", "programmer"),
    ("chuch", "dancer"),
    ("chuch", "translator"),
    ("ship", "programmer"),
    ("ship", "dancer"),
    ("ship", "singer"),
    ("ribb", "programmer"),
    ("ribb", "artist")
]
cur.execute('SELECT * FROM users')
con.commit()
print(cur.fetchall())
cur.execute('SELECT * FROM professions')
con.commit()
print(cur.fetchall())
for i in var_list_user_profession:
    cur.execute(f"SELECT id FROM users WHERE name ='{i[0]}';")
    id1 = cur.fetchall()
    cur.execute(f"SELECT id FROM professions WHERE name = '{i[1]}';")
    id2 = cur.fetchall()
    cur.execute('INSERT INTO user_profession(user_id, profession_id) VALUES (?,?)', (id1[0][0], id2[0][0],))
    con.commit()
cur.execute('SELECT * FROM user_profession')
print(cur.fetchall())
cur.execute('SELECT name FROM professions')
var_list = []
for i in cur.fetchall():
    var_list.append(i[0])
print(var_list)
cur.execute(f"SELECT id FROM professions WHERE name ='{var_list[0]}';")
id2 = cur.fetchall()[0][0]
print(id2)
print(cur.lastrowid)