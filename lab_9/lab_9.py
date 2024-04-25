"""
Вариант 5 Дан файл в формате csv. (Фамилия, Имя, Учреждение
(организация), Отдел, Адрес электронной почты, Состояние, Тест начат,
Завершено, Затраченное время, Оценка/100,00, В.1 /10,00, В.2 /10,00, В.3
/10,00, В.4 /10,00, В.5 /10,00, В.6 /10,00, В.7 /10,00, В.8 /10,00, В.9 /10,00, В.10
/10,00).
Примечание: Тест считается пройденным, если набрано 6/10 (60/100)
баллов.
Примечание: Поля «Тест начат», «Завершено» заданы в формате «12
Май 2017 10:09», поле «Затраченное время» в формате «31 мин. 22 сек.».
Вывести список слушателей в порядке времени выполнения теста,
начиная с самого наименьшего.
"""

import pandas as pd


def time_to_seconds(time_str):
    mas_time = []
    for time in time_str:
        time = str(time)
        time = time.replace(' мин.', '').replace(' сек.', '').split()
        if time[0] != 'nan':
            mas_time.append(int(time[0]) * 60 + int(time[1]))

    return pd.Series(mas_time)


data = pd.read_csv("5 - 1.csv")
'''result = data[time_to_seconds(data.get("Затраченное время", ""))].reset_index()'''
data.insert(1, 'NewCol', time_to_seconds(data.get("Затраченное время", "")))
print(len(data))
print(data.sort_values(by='NewCol'))
data = pd.read_csv("5 - 2.csv")
'''result = data[time_to_seconds(data.get("Затраченное время", ""))].reset_index()'''
data.insert(1, 'NewCol', time_to_seconds(data.get("Затраченное время", "")))
print(len(data))
print(data.sort_values(by='NewCol'))


