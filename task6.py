# Массив имеет четное число элементов N.
# Заполнить массив случайными числами и
# выполнить реверс отдельно в первой половине и второй половине.
# Пример: ввод N = 6
# [1,2,3,4,5,6]
# Вывод: [3,2,1,6,5,4]
from random import randint
n = int(input())
mas = [randint(0,1000) for i in range(n)]
print(mas)
a = mas
a.reverse()
a=a[0:n//2]
mas = mas [n//2:]
result = mas + a
<<<<<<< HEAD
print(result)
=======
print(result)
>>>>>>> 8faa1b3e8d72c09201fa3262514ed4bfd49bc206
