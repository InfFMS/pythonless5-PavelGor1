from random import  randint
N=int(input())
my_list = [randint(0,1000) for i in range(N)]
arif = sum(my_list)//N
my_list.sort()
print(my_list)
for item in my_list.copy():
    if item > 1.3*arif:
        my_list.remove(item)
    elif item < 0.7*arif:
        my_list.remove(item)
print(my_list)
