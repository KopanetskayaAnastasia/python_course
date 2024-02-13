import random
import re
from array import *


# Task1.v5.1: найти кол-во делителей числа, не делящихся на 3
def func_1(n):
    k = 0
    for i in range(1, n+1):
        if n % i == 0 and i % 3 != 0:
            k += 1
    return k


num = int(input('Enter the number for count of divisors of number not divisible by 3: '))
print(func_1(num))


# Task1.v5.2: найти минимальную нечетную цифру числа
def func_2(n):
    t = n % 10
    n //= 10
    while n != 0:
        k = n % 10
        if (k % 2 == 1 and k < t and t % 2 == 1) or (k % 2 == 1 and t % 2 == 0):
            t = k
        n //= 10
    if t % 2 == 0:
        return "No odd number"
    else:
        return t


num = int(input('Enter the number for the minimum odd digit: '))
print(func_2(num))


# Task1.v5.3: найти сумму всех делителей числа, взаимно простых с суммой цифр числа и не взаимно простых  с произведением цифр числа
def func_3(n):
    sum_number = 0
    comp_number = 1
    n1 = n
    while n1 != 0:
        sum_number += n1 % 10
        comp_number *= n1 % 10
        n1 //= 10
    del_n = array('i', [])
    for i in range(1, n + 1):
        if n % i == 0:
            del_n.append(i)
    summ = 0
    for i in del_n:
        k1 = True
        k2 = False
        for j in range(2, i + 1):
            if i % j == 0 and sum_number % j == 0:
                k1 = False
            if i % j == 0 and comp_number % j == 0:
                k2 = True
        if k1 is True and k2 is True:
            summ += i
    return summ


num = int(input('Enter the number for the amount... : '))
print(func_3(num))


# Task2-4.v5.5: дана строка, перемешать все символы в случайном порядке
def func_5(n):
    a = []
    for i in n:
        a.append(i)
    random.shuffle(a)
    s = ''
    for i in a:
        s += i
    return s


num = str(input('Enter the string to shuffle: '))
print(func_5(num))


# Task2-4.v5.7: дана строка, состоящая из символов латиницы. необходимо проверить, образуют ли прописные символы этой строки палиндром
def func_7(n):
    k = True
    for i in n:
        if not re.search(r'[A-Za-z\s]', i):
            k = False
    s = ''
    if k is True:
        for i in n:
            if i.isupper():
                s += i
    else:
        return "Error, use only Latin letters"
    if s != '':
        return s == s[::-1]
    else:
        return "There is no uppercase palindrome in the string"


num = str(input('Is this a palindrome: '))
print(func_7(num))


# Task2-3.v5.14: дана строка, в которой записаны слова через пробел. необх упоряд слова по кол-ву букв в каждом слове
def func_14(n):
    s = n.split()
    k = ''
    for i in sorted(s, key=len):
        k += i
        k += ' '
    return k


num = str(input('Enter the string to sort by quantity: '))
print(func_14(num))


# Task5: дана строка, найти все даты, которые описаны в виде "31 февраля 2024"
def func_data(n):
    k = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    result = []
    for i in re.findall(r'\d{1,2} \w{3,8} \d\d\d\d', n):
        s = i.split()
        if k.__contains__(s[1]) and 1 <= int(s[0]) <= 31:
            result.append(i)
    return result


num = str(input('Enter the string for search data: '))
print(func_data(num))


# Task6-8.v5.5: дана строка, необходимо найти наибольшее количество идущих подряд символов кириллицы
def func_6_5(n):
    cur_len = 0
    max_len = 0
    for i in n:
        if re.search(r'[А-ЯЁа-яё]', i):
            cur_len += 1
            if cur_len > max_len:
                max_len = cur_len
        else:
            cur_len = 0
    return max_len


# Task6-8.v5.7: дана строка, необходимо найти минимальное из имеющихся в ней натуральных чисел
def func_7_7(n):
    k = []
    k1 = ''
    for i in n:
        if re.search(r'[0-9]', i):
            k1 += i
        else:
            if k1 != '':
                k.append(int(k1))
            k1 = ''
    return min(k)


# Task6-8.v5.14: дана строка, необходимо найти наибольшее количество идущих подряд цифр
def func_8_14(n):
    cur_len = 0
    max_len = 0
    for i in n:
        if re.search(r'[0-9]', i):
            cur_len += 1
            if cur_len > max_len:
                max_len = cur_len
        else:
            cur_len = 0
    return max_len


print("Enter the task number from: {5, 7, 14}")
n = int(input())
if n == 5:
    num = str(input('Enter the string for max_len of kirillitsa: '))
    print(func_6_5(num))
if n == 7:
    num = str(input('Enter the string for min_value of N numbers : '))
    print(func_7_7(num))
if n == 14:
    num = str(input('Enter the string for max_len of numbers : '))
    print(func_8_14(num))


# Task9: Прочитать список строк с клавиатуры, упорядочить по длине строк
n = int(input('Enter number of lines: '))
s = []
for i in range(n):
    k = str(input('Enter the string: '))
    s.append(k)
print('Ordered by number of lines: ')
print("\n".join(sorted(s, key=len)))


# Task10: Прочитать список строк с клавиатуры, упорядочить по количеству слов в строке
n = int(input('Enter number of lines: '))
s = []
for i in range(n):
    k = str(input('Enter the string: '))
    k = k.split()
    s.append(k)
s = sorted(s, key=len)
print('Ordered by number of words per line: ')
for i in range(n):
    s[i] = " ".join(s[i])
print("\n".join(s))


# Task11-14.v5.2: отсортировать строку в порядке увеличение
# среднего веса ASCII кода строки
def avg_ascii(k):
    a = 0
    for i in k:
        a += ord(i)
    return a/len(k)


def func_11_2(s, n):
    a = []
    for i in s:
        a.append([avg_ascii(i), i])
    a = sorted(a)
    return a


# Task11-14.v5.6: В порядке увеличения медианного значения выборки строк
# (прошлое медианное значение удаляется из выборки и производится поиск нового медианного значения)
def func_12_6(s,n):
    a = []
    while s:
        m = 0
        i_cur = 0
        for i in s:
            if len(i) % 2 == 0:
                if m == 0 or (ord(i[n // 2]) + ord(i[n // 2 + 1])) / 2 < m:
                    m = ord(i[n // 2]) + ord(i[n // 2 + 1]) / 2
                    i_cur = i
            else:
                if m == 0 or ord(i[n // 2 + 1]) < m:
                    m = ord(i[n // 2 + 1])
                    i_cur = i
        a.append(i_cur)
        s.remove(i_cur)
        n -= 1
    return a


# Task11-14.v5.8: В порядке увеличения квадратичного отклонения между средним
#весом ASCII-кода символа в строке и максимально среднего ASCII-кода
#тройки подряд идущих символов в строке.
def func_13_8(s, n):
    a = []
    for i in s:
        max_w = 0
        for j in range(len(i)-2):
            if (ord(i[j]) + ord(i[j+1]) + ord(i[j+2])) > max_w:
                max_w = ord(i[j]) + ord(i[j+1]) + ord(i[j+2])
        a.append([(avg_ascii(i) - max_w / 3) ** 2, i])
    a = sorted(a)
    return a


# Task11-14.v5.12: в порядке увеличения квадратичного отклонения
# частоты встречаемости самого распространенного символа в наборе строк
# от частоты его встречаемости в данной строке
def func_14_12(s, n):
    dif_symbol = ''
    n1 = 0
    for i in s:
        n1 += len(i)
        for j in i:
            if dif_symbol.find(j) == -1:
                dif_symbol += j
    a = ''.join(s)
    c1 = []
    m0 = 0
    m1 = ''
    for k in dif_symbol:
        if a.count(k) > m0:
            m0 = a.count(k)
            m1 = k
    c = []
    for i in s:
        c.append([(m0/n1 - i.count(m1)/len(i))**2, i])
    return sorted(c)


print("Enter the task number from: {2, 6, 8, 12}")
n = int(input())
num = int(input('Enter number of lines: '))
s = []
for i in range(num):
    s.append(str(input('Enter the string: ')))
if n == 2:
    print(func_11_2(s, num))
if n == 6:
    print(func_12_6(s,num))
if n == 8:
    print(func_13_8(s,num))
if n == 12:
    print(func_14_12(s, num))