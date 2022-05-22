''' 
Para cada i entre len(A) y 1 (inclusive):
Buscar el mayor elemento en A[:i].
Intercambiarlo con A[i-1].
'''

from typing import List

def pos_mayor_elemento(B:List[int]) -> int:
    pos_mayor:int = 0
    for i,value in enumerate(B):
        if value > B[pos_mayor]:
            pos_mayor = i
    return pos_mayor

def selection_sort(A:List[int]):
    for i in range(len(A),2,-1):
        pm:int = pos_mayor_elemento(A[:i])
        A[pm], A[i-1] = A[i-1], A[pm] 
    return A
