# вариант 5
# почтовый индекс - 6 идущих подряд цифр

import re
pattern = re.compile(r"\d{6}", re.I)


def check_index(ind) -> bool:
    return bool(pattern.fullmatch(ind))


'''index = str(input())
print(check_index(index))'''


def check_index_ex(ind):
    try:
        if check_index(ind):
            print(ind)
        else:
            raise Exception('Почтовый индекс некорректен')
    except Exception:
        print('Введите корректный почтовый идекс. ', ind, '- некорректный ')


index = str(input())
check_index_ex(index)

