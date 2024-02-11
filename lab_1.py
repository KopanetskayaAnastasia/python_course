import random
import re
from array import *


#Task1.v5.1: найти кол-во делителей числа, не делящихся на 3
def func_1(n):
    k = 0
    for i in range(1, n+1):
        if n % i == 0 and i % 3 != 0:
            k += 1
    return k


num = int(input('Enter number: '))
print(func_1(num))


#Task1.v5.2: найти минимальную нечетную цифру числа
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


num = int(input('Enter number: '))
print(func_2(num))


#Task1.v5.3: найти сумму всех делителей числа, взаимно простых с суммой цифр числа и не взаимно простых  с произведением цифр числа
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


num = int(input('Enter number: '))
print(func_3(num))


#Task2-4.v5.5: дана строка, перемешать все символы в случайном порядке
def func_5(n):
    a = []
    for i in n:
        a.append(i)
    random.shuffle(a)
    s = ''
    for i in a:
        s += i
    return s


num = str(input('Enter string: '))
print(func_5(num))


#Task2-4.v5.7: дана строка, состоящая из символов латиницы. необходимо проверить, образуют ли прописные символы этой строки палиндром
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
    return s == s[::-1]


num = str(input('Is it palindrome: '))
print(func_7(num))


#Task2-3.v5.14: дана строка, в которой записаны слова через пробел. необх упоряд слова по кол-ву букв в каждом слове
def func_14(n):
    s = n.split()
    k = ''
    for i in sorted(s, key=len):
        k += i
        k += ' '
    return k

num = str(input('Enter string: '))
print(func_14(num))

