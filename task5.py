# Введите массив длины N с клавиатуры и найдите (за один проход)
# количество элементов, имеющих максимальное значение.
<<<<<<< HEAD
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
=======
mas = [1,2,3,4]
for i in range(2):
    mas.reverse()
print(mas)
>>>>>>> 8faa1b3e8d72c09201fa3262514ed4bfd49bc206
