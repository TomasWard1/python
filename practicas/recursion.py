from re import L
from sys import exc_info
from typing import List, Tuple
################
# EJERCICIO 1 (a)
################

def potencia_de_3_a_n(n: int) -> int:
    '''Requiere: n natural
    Devuelve: 3^n
    '''
    if n == 0:
        return 1
    else:
        return 3*potencia_de_3_a_n(n-1)

#print(potencia_de_3_a_n(3))
    

################
# EJERCICIO 1 (b)
################

def resto_division_por_cinco(n: int) -> int:
    '''Requiere: n natural
    Devuelve: el resto de dividir a n por 5
    '''
    if n < 5:
        return n
    else:
        return resto_division_por_cinco(n-5)

#print(resto_division_por_cinco(15))
    


################
# EJERCICIO 2
################

def es_capicua_normal(xs:List[int]) -> bool:
    '''
    Requiere: nada
    Devuelve: True si xs es una lista de números capicua (es la misma si se lee tanto al derecho como al revés);
              False en caso contrario
    '''
    if (xs[::-1] == xs):
            return True
    return False 

def es_capicua(xs:List[int]) -> bool:
    '''
    Requiere: nada
    Devuelve: True si xs es una lista de números capicua (es la misma si se lee tanto al derecho como al revés);
              False en caso contrario
    '''
    if len(xs) == 0:
        return True
    else:
        extremos_iguales:bool = xs[0] == xs[len(xs)-1]
        if extremos_iguales:
            return es_capicua(xs[1:len(xs)-1])
        return False 

# print(es_capicua([]))
# print(es_capicua([1]))
# print(es_capicua([1,2,22,22,2,1]))
################
# EJERCICIO 3 
################
    
def contar_letras(xs:List[str], l:str) -> int:
    '''
    Requiere: nada
    Devuelve: la cantidad de cadenas en xs que contienen la letra l
    '''
    if len(xs) == 0:
        return 0
    else:
        if l in xs[0]:
            return contar_letras(xs[1:],l) + 1
        return 0
    
#print(contar_letras(['a'],''))

def ejercicio_parcial(xs:List[int]):
    if len(xs) == 0:
            return 0
    else:
        es_positivo:bool = xs[0] > 0
        if es_positivo:
            return ejercicio_parcial(xs[1:]) + xs[0]
        else:
            return ejercicio_parcial(xs[1:])

#print(ejercicio_parcial([1,2,-3,4]))
