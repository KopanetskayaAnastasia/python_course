#!/usr/bin/env python3
import cgi
import html
import sqlite3


# Задаем переменные
print("Content-Type: text/html; charset=utf-8\r")
form = cgi.FieldStorage()
user_name = form.getfirst("name", "не задано")
user_email = form.getfirst("email", "не задано")
user_phone = form.getfirst("phone", "не задано")
profession_name = form.getfirst("profession", "не задано")
created_at = form.getfirst("data", "не задано")

print("""<!DOCTYPE HTML>
<html>

<head>
	<meta name="viewport" content="text/html;charset=utf-8" http-equiv="Content-Type">
	<title>Кадровое агенство</title>
</head>
<body>
    <form action="/cgi-bin/form.py">
        <h2>Введите данные</h2>
        <fieldset>
            <ul>
                <li>
                    <label for="user_name">Имя:</label>
                    <input type="text" name="name" id="user_name" required>
                </li>
                <li>
                    <label for="user_phone">Телефон:</label>
                    <input type="text" name="phone" id="user_phone" required>
                </li>
                <li>
                    <label for="user_email">Email:</label>
                    <input type="text" name="email" id="user_email" required>
                </li>
                <li>
                    <label for="profession_name">Профессия:</label>
                    <input type="text" name="profession" id="profession_name" required>
                </li>
                <li>
                    <label for="created_at">Дата регистрации:</label>
                    <input type="text" name="data" id="created_at" required>
                </li>
            </ul>
            <button type="submit">Отправить данные</button>
        </fieldset>

    </form>
""")
if form.getvalue('name') and form.getvalue('email') and form.getvalue('phone') and form.getvalue(
        'profession') and form.getvalue('data'):
    print("<p>Запрос отправлен</p>")

# Код
con = sqlite3.connect('db01.db')
cur = con.cursor()
cur.execute('INSERT INTO users(name,phone,email, created_at) VALUES(?,?,?,?)', (user_name, user_phone, user_email, created_at,))
con.commit()
id1 = cur.lastrowid
cur.execute('SELECT name FROM professions')
id2 = 0
var_list = []
for i in cur.fetchall():
    var_list.append(i[0])
if profession_name not in var_list:
    cur.execute('INSERT INTO professions(name) VALUES(?)', (profession_name, ))
    con.commit()
    id2 = cur.lastrowid
else:
    cur.execute(f"SELECT id FROM professions WHERE name ='{profession_name}';")
    id2 = cur.fetchall()[0][0]
cur.execute('INSERT INTO user_profession(user_id, profession_id) VALUES (?,?)', (id1, id2,))
con.commit()

# Вывод данных таблиц
cur.execute('SELECT * FROM users')
us = cur.fetchall()
print('<h1>Зарегестрированныые кадры<h1><br>')
for i in us:
    print('Имя: '+i[1]+'<br>')
    print('Телефон: ' + i[2]+'<br>')
    print('Email: ' + i[3]+'<br>')
    print('Дата регистрации: ' + i[4]+'<br>')
    print('******************'+'<br>')

cur.execute('SELECT * FROM professions')
us = cur.fetchall()
print('<h1>Профессии<h1><br>')
for i in us:
    print(i[1]+'<br>')

cur.execute('SELECT * FROM user_profession')
us = cur.fetchall()
print('<h1>Кадры и их должности<h1><br>')
for i in us:
    cur.execute(f"SELECT name FROM users WHERE id ={i[1]};")
    name1 = cur.fetchall()
    cur.execute(f"SELECT name FROM professions WHERE id ={i[2]};")
    name2 = cur.fetchall()
    print('Имя кадра: '+name1[0][0]+'<br>')
    print('Название професии: ' + name2[0][0]+'<br>')
    print('******************'+'<br>')

print("""</body>
        </html>""")

