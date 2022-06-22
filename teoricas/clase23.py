#Recursion algoritmica
import time
from typing import List

def despegue(tiempo:int):
    if tiempo != 0:
        print('hola ' + str(tiempo))
        time.sleep(1)
        despegue(tiempo-1)
    else:
        print('Despegue!')

def suma(n:int) -> int:
    '''
    Requiere: n >= 0
    '''
    if n == 0:
        return 0
    else:    
        return suma(n-1) + n

# def maximo(lista:List[int],max:int) -> int:
#     if len(lista) == 0:
#         return max
#     else:
#         if lista[0] > max:
#             max = lista[0]
#         return maximo(lista[1:],max)

def maximo(lista:List[int]) -> int:
    '''
    Requiere: lista no vacia
    '''
    if len(lista) == 1:
        return lista[0]
    else:
        max:int = maximo(lista[1:])
        if lista[0] > max:
            return lista[0]
        else:
            return max 

print(maximo([70,20,4340]))
    