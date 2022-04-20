
from typing import List

def es_primo(n:int) -> bool:
    ''' 
    Requiere: n > 1, n sea numero natural.
    Devuelve: True si n es primo (es divisible unicamente por n y por 1)
    False en lo contrario.
    '''
    divisor:int = 2
    esPrimo:bool = True
    while divisor < n:
        if n % divisor == 0:
            esPrimo = False
        divisor += 1
    return esPrimo

números:List[int] = [10, 9, 13, 70, 9, 11, 18, 21, 19]
pos_primos:List[int] = []
for i in range(len(números)):
    if es_primo(números[i]):
        pos_primos.append(i)
print("Hay primos en las posiciones:", pos_primos)
