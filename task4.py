# При анализе данных, собранных в рамках научного эксперимента,
# бывает полезно удалить самое большое и самое маленькое значение.
# Сымитруем данные списком длины N со случайными числами в диапазоне от 0 до 1000
# Удалите из этого списка все значения, которые на 30 % отличаются
# от среднего значения списка
from random import randint
N = int(input())
mas = [randint(0,1000) for i in range(N)]
udal = 0
arifmet = sum(mas)//N
print(mas)
for i in range(N-1):
    if mas[i] > 1.3*arifmet or mas[i] < 0.7*arifmet:
        mas[i]=udal
string = ''
for el in mas:
    string += str(el)
print(string)
string.find('0')
