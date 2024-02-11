import random
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
    for i in range(1, n):
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


