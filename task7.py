# Заполнить массив длины N случайными числами в интервале [-100,100] и
# переставить элементы так, чтобы все положительные элементы
# стояли в начала массива, а все отрицательные и нули в конце.
# Пример: ввод N = 6
# [20, -90, 15, -34, 10, 0]
# Вывод: [20, 15, 10, -90, -34, 0]
from random import randint
n = int(input())
<<<<<<< HEAD
mas = [randint(-1,1) for i in range(n)]
print(mas)
mas.sort()
mas.reverse()
s=0
for i in mas.copy():
    if i==0:
        mas.remove(i)
        s +=1
mas=mas+[0]*s
print(mas)
=======
mas = [randint(-100,100) for i in range(n)]
for i in range(n-1):
    if mas[i]>0:
        mas = mas[:i:-1]
print(mas)
>>>>>>> 8faa1b3e8d72c09201fa3262514ed4bfd49bc206
