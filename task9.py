# Напишите программу, которая удаляет дубликаты из списка длины N.
# Пример работы:
# Пример: ввод N = 8
# [10, 20, 10, 20, 30, 40, 30, 50]
# После удаления дублей:  [10, 20, 30, 40, 50]
from random import randint
n = int(input())
mas = [randint(10,11) for i in range(n)]
print (str(mas))
mas= list(set(mas))
print (str(mas))
