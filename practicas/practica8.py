
from typing import List


def suma_en_posiciones_impares(lista:List[int],n:int) -> List[int]:
    i:int = 0
    newList:List[int] = []

    for i,value in lista:
        print(i)

    while i < len(lista):
        print(lista[i])
        i +=1


suma_en_posiciones_impares([],3)