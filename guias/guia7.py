'''
Ejercicio 1. Se tiene un mazo de M naipes. Escribir un algoritmo que determine si el mazo está
ordenado (de menor a mayor) o no. Calcular su complejidad algorítmica (en peor caso).
'''

import enum
import math
from statistics import median
from typing import List


def mazoOrdenado(naipes: List[int]):
    mayorNaipe: int = 0  # O(1)
    m: int = len(naipes)  # O(1)
    for carta in naipes:  # O(M)
        if carta >= mayorNaipe:  # O(1)
            mayorNaipe = carta  # O(1)
        else:
            return False  # O(1)
    return True  # O(1)


'''
Operando los ordenes:
O(1) + O(1) +(O(M)x O(max(1,1,1))) + O(1) = 
O(1) + O(1) +(O(M)x O(1)) + O(1) = 
O(1) + O(1) + O(M) + O(1) = 
O(max(1,1,M,1)) = 
O(M) --> Orden del algoritmo mazoOrdenado()
'''


def contenido_cuanto(string_1: str, string_2: str):
    return len(string_2.split(string_1)) - 1


'''
El algoritmo BUBBLESORT consiste en recorrer la lista A de izquierda a derecha, dejando
ordenado en cada paso al par de elementos A[i] y A[i+1]. Esta pasada por toda la lista
debe repetirse len(A) veces. Implementar el algoritmo en Python. ¿Por qué funciona?
'''


def bubble_sort(a: List[int]) -> List[int]:
    for i in range(len(a)-1):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a


'''
Escribir un programa que, dados una lista de enteros A y un entero x, retorne todos los
elementos de A menores o iguales que x. Estimar su complejidad algorítmica (en peor caso).
'''


def menor_o_igual(enteros: List[int], x: int):
    res: List[int] = []
    for entero in enteros:
        if entero <= x:
            res.append(entero)
    return res


'''
Igual al punto anterior, pero sabiendo que la lista está ordenada.
'''


def menor_o_igual_ordenada(enteros: List[int], x: int):
    for i, entero in enumerate(enteros):
        if entero == x:
            return enteros[:i+1]
        elif entero > x:
            return enteros[:i]
    return []


'''
(a) Calcular la media de una lista A de enteros. O(len(A))
'''


def media(lista: List[int]):
    sumatoria: int = 0
    for numero in lista:
        sumatoria += numero
    return sumatoria//len(lista)


'''
(b) Calcular la mediana de una lista A de enteros. O(len(A)2)
'''

def mediana(lista: List[int]):
    bubble_sort(lista)
    print(lista)
    if len(lista) % 2 == 0:
        valor_del_medio_izq:int = lista[(len(lista)//2)-1]
        valor_del_medio_der:int = lista[(len(lista)//2)]
        return (valor_del_medio_der + valor_del_medio_izq)/2
    else:
        return lista[len(lista)//2]

'''
(c) Determinar, dado un n natural, si n es (o no) primo. O(√n)
'''

def es_primo(natural:int):
    for i in range(2,int(math.sqrt(natural)+1)):
        if natural % i == 0:
            return False
    return natural != 1 and True

'''
(d) Dada una lista A de 1s y 0s representando un número en base binaria, obtener el número
correspondiente en base decimal. O(len(A))
'''


def binario_a_decimal(binario:List[int]):
    decimal:int = 0
    binario = binario[::-1]
    for i,bit in enumerate(binario):
        if bit == 1:
            decimal += pow(2,i)
    return decimal

'''
(e) Dada una lista de enteros ordenada de menor a mayor, devolver True si todos sus elementos
son positivos, o False si hay algún elemento negativo. O(1)
'''

