# Введите массив длины N с клавиатуры и найдите (за один проход)
# количество элементов, имеющих максимальное значение.
from random import randint
n = int(input())
mas = [randint(0, 1000)for i in range(n)]
a = max(mas)
print(a,'- максимальное значение')
print(mas)
s= 0
for i in range(n):
    if a == mas[i]:
        s += 1
print(s,'- кол-во совпадающих чисел')
