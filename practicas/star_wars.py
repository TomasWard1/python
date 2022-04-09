from typing import List
import unittest

def nave_estelar_cercana(sensado:List[int],p:int) -> bool:
    '''
    Requiere: Lista no vacia de enteros >= 0 (sensado), p >= 0
    Devuelve: True si existe algun numero del sensado es menor o igual a p.
    '''
    i:int = 0
    naveEstelarCerca:bool = False
    while i < len(sensado):
        if sensado[i] <= p:
            naveEstelarCerca = True
        i += 1

    return naveEstelarCerca


#Terminacion 1
'''
- La variable i:int comienza valiendo 0.
- La condicion del while dice que el ciclo correrá mientras i < len(sensado).
- Sabemos que len(sensado) no se modifica.
- En cada iteracion del ciclo, i se incrementa por 1.
- Eventualmente i == len(sensado), lo cual hará falsa la condicion del while.
- El ciclo termina.
'''

#Invariante 1
'''
0 <= i <= len(sensado)
naveEstelarCerca es un booleano que será True si i elementos
de la lista sensado son menores o iguales a p, False en lo contrario.

- En el punto #A i = 0, 0 elementos se analizaron de la lista sensado entonces
naveEstelarCerca es False.
- Primer Iteración del ciclo
    - En el punto #B de la primera iteracion del ciclo i = 0,
    0 elementos se analizaron de la lista sensado entonces
    naveEstelarCerca es False.
    - En el punto #C de la primera iteracion del ciclo i = 1,
    1 elementos se analizaron de la lista sensado entonces
    naveEstelarCerca es False si el primer elemento es mayor a p, True en la inversa.
- Proximas iteraciones: Va a ocurrir lo mismo que lo anterior.
- En el punto #D, i == len(sensado) y se analizaron todos los elementos de la lista sensado entonces
naveEstelarCerca es False si ninguno de los elementos fue menor o igual a p, True
en lo contrario.
'''


