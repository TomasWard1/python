# Programa 3
from typing import List

a: List[int] = [1, 2]
b: List[int] = a
a.append(3)
#print(a,b)

p: bool = True
q: bool = p
p = False
#print(p,q) #False,True

bs1: List[bool] = [True, False]
bs2: List[bool] = bs1
bs2.pop()
bs2.pop()

#print(bs1,bs2) #[] []


# Programa 4
def f(m: int):
    m = m + 1


n: int = 1000
f(n)

#print(n)


# Programa 6
def h(b: List[bool]):
    b.append(False)


a: List[bool] = [True, True]
h(a)
#print ( a )


def cuenta_regresiva(n: int) -> str:
    vr: str = ' '
    while n > 0:
        vr = vr + str(n)
        n = n - 1
    return vr


def evanesco(cosas: List[str]):
    while len(cosas) > 0:
        cosas.pop()


num: int = 5
print(num, cuenta_regresiva(num), num) #5, 54321, 5


items: List[str] = [' pergamino ', ' poción ', ' serpiente ']

print(items.pop())
print(items)
evanesco(items)
print(items) #[]

