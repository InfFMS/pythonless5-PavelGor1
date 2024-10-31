
def f(m):
    ans=[]
    for i in m:
        if str(i)==len(str(i))*str(i)[0]:
            ans.append(i)
    return ans
from random import randint
n = int(input())
mas = [randint(10,100000) for i in range(n)]
print(f(mas))
