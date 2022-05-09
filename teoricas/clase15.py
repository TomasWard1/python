'''
1. Escribir un algoritmo en pseudocódigo que busque un A♥ en N
naipes. Analizar su complejidad algorítmica en el peor caso

Contar A♥ en N naipes:
    aparece = False
    i = 0
    mientras i < N:
        dar vuelta el naipe i
        si el naipe es == A♥:
            aparece = True
        sumar 1 a i 
    devolver aparece

2. Si se corta la ejecución al encontrar un A♥, cambia la complejidad
en el peor caso?
La complejidad siempre va a ser siempre de orden lineal, O(N), aunque el A♥
aparezca al final.
'''
from typing import List

def buscar(elem:int, lista:List[int]) -> bool:
    for item in lista:
        if item == elem:
            return True
    return False

