from collections import Counter
from typing import List
import unittest

# EJERCICIO 3 --------------------------------


def eslistaCreciente(lista: List[int]) -> bool:
    i: int = 0
    esEstrictamenteCreciente: bool = True

    while i < len(lista) - 1:
        numActual: int = lista[i]
        numProximo: int = lista[i+1]
        if numActual >= numProximo:
            esEstrictamenteCreciente = False
        i += 1

    return esEstrictamenteCreciente


class TestCreciente(unittest.TestCase):
    def test_estrictoCreciente(self):
        self.assertEqual(eslistaCreciente([1, 2, 3, 4, 5]), True)
        self.assertEqual(eslistaCreciente([5, 7, 8, 19]), True)
        self.assertEqual(eslistaCreciente([100, 101, 102, 103, 104]), True)

    def test_creciente(self):
        self.assertEqual(eslistaCreciente([1, 2, 2, 2, 5]), False)
        self.assertEqual(eslistaCreciente([5, 5, 5, 80, 90]), False)
        self.assertEqual(eslistaCreciente([100, 101, 101, 103, 104]), False)

    def test_decrecienteEstricto(self):
        self.assertEqual(eslistaCreciente([6, 5, 4, 3, 2, 1]), False)
        self.assertEqual(eslistaCreciente([90, 80]), False)

    def test_decreciente(self):
        self.assertEqual(eslistaCreciente([6, 5, 5, 5, 2, 1]), False)
        self.assertEqual(eslistaCreciente([5, 5, 5, 3, 2]), False)
        self.assertEqual(eslistaCreciente([100, 100, 99]), False)

    def test_cambio(self):
        self.assertEqual(eslistaCreciente([1, 2, 3, 2]), False)
        self.assertEqual(eslistaCreciente([3, 2, 1, 2, 3]), False)

    def test_otros(self):
        self.assertEqual(eslistaCreciente([]), True)
        self.assertEqual(eslistaCreciente([5]), True)
        self.assertEqual(eslistaCreciente([100, 100, 100]), False)


def separarStringconSeparador(txt: str, sep: str):
    '''
    Requiere: len(sep) == 1
    Devuelve: Una nueva lista de str en donde cada elemento es la separacion de txt
    a partir de un separador sep.
    '''
    listaSeparada: List[str] = []

    i: int = 0
    entrada: str = ''
    while i < len(txt):
        if txt[i] != sep:
            entrada += txt[i]
        else:
            listaSeparada.append(entrada)
            entrada = ''
        i = i + 1
    listaSeparada.append(entrada)
    return listaSeparada


class TestSeparador(unittest.TestCase):
    def test_punto(self):
        self.assertEqual(separarStringconSeparador(
            'a.b.c', '.'), ['a', 'b', 'c'])

    def test_coma(self):
        self.assertEqual(separarStringconSeparador(
            'a,b,c', ','), ['a', 'b', 'c'])

    def test_separador_prePost(self):
        self.assertEqual(separarStringconSeparador(
            ',a,b,c,', ','), ['', 'a', 'b', 'c', ''])
        self.assertEqual(separarStringconSeparador(
            '.a.b.c.', '.'), ['', 'a', 'b', 'c', ''])


# EJERCICIO 4 ---------------------------------
def encontrarMesetas(lista: List[int]) -> List[List[int]]:
    '''
    Requiere: len(Lista[int]) > 0
    Devuelve: List[List[int]], una lista de las mesetas contenidas en la lista inicial.
    '''
    i: int = 1
    mesetas: List[List[int]] = []
    while i < len(lista):
        meseta: List[int] = [lista[i-1]]

        while i < len(lista) and lista[i] in meseta:
            meseta.append(lista[i])
            i += 1

        mesetas.append(meseta)
        i += 1

    return mesetas

# EJERCICIO 9 ----------------------------------------


def a(lista: List[float]) -> float:
    ''' 
    Requiere: Lista no vacia de tipo float
    Devuelve: un float que corresponde al valor maximo de la lista
    queremos que itere en cada valor
    Compara cada valor con el anterior
    Almacena el valor mas grande en una variable
    si es mas grande cambia el valor de esa variable, sino no
    '''
    valorMasGrande: int = 0
    for numero in lista:
        if numero > valorMasGrande:
            valorMasGrande = numero
    return valorMasGrande


def b(lista=List[str]) -> str:
    '''
    Requiere: Nada
    Devuelve: Un str que es la concatenacion de todos los elemntos de la lista en el argumento.
    '''
    res: str = ''
    for string in lista:
        res += string

    return res


def c(lista=List[int]) -> bool:
    '''
    Requiere: Nada
    Devuelve: Un bool que es True si la lista de enteros esta ordenada
    estrictamente creciente. False en lo contrario
    '''
    estrictamenteCreciente: bool = True
    enteroAnterior: int = 0
    for entero in lista:
        if entero <= enteroAnterior:
            estrictamenteCreciente = False
            break
        enteroAnterior = entero
    return estrictamenteCreciente


def d(n: int) -> List[int]:
    '''
    Requiere: n sea un numero natural, n > 0
    Devuelve: Una lista con los primeros n numeros naturales impares
    ordenados de menor a mayor.
    '''
    naturalesImpares: List[int] = []
    for i in range(n*2):
        if (i % 2 != 0):
            naturalesImpares.append(i)
    return naturalesImpares

print(d(4))

def e(listaEnteros: List[int], n: int) -> List[int]:
    '''
    Requiere: n sea entero.
    Devuelve: Una lista que contiene cada elemento de la lista original
    adicionado en n.
    '''
    nuevaLista: List[int] = []
    for entero in listaEnteros:
        nuevaLista.append(entero+n)
    return nuevaLista


def f(lista: List[str]) -> int:
    '''
    Requiere: Nada
    Devuelve: int que es la cantidad de caracteres de la totalidad
    de elementos en la lista del argumento.
    '''
    contadorCaracteres: int = 0
    for string in lista:
        for caracter in string:
            contadorCaracteres += 1
    return contadorCaracteres


def g(lista: List[str]) -> int:
    '''
    Requiere: Nada
    Devuelve: int que es la cantidad de veces que aparece la letra a en cualquier elemento
    de la lista.
    '''
    contadorA: int = 0
    for string in lista:
        for caracter in string:
            if caracter == 'a':
                contadorA += 1
    return contadorA


def h(txt: str, sep: str) -> int:
    '''
    Requiere: len(sep) == 1
    Devuelve: Una lista que contiene la separacion de txt
    a partir de sep.
    '''
    slice: str = ''
    nuevaLista: List[str] = []
    for caracter in txt:
        if caracter != sep:
            slice += caracter
        else:
            nuevaLista.append(slice)
            slice = ''
    nuevaLista.append(slice)
    return nuevaLista


def h2(txt: str, sep: str) -> int:
    '''
    Requiere: len(sep) == 1
    Devuelve: Una lista que contiene la separacion de txt
    a partir de sep.
    '''
    nuevaLista: List[str] = []
    for slice in txt.split(sep):
        nuevaLista.append(slice)
    return nuevaLista

print(h2('aaa;bb;c;d;',';'))
# EJERCICIO 10-----------------------------------------------------------------------------


def buscar_v1(elem: int, ls: List[int]) -> bool:
    '''
    Requiere : nada .
    Devuelve : True sii elem aparece al menos una vez en ls.
    '''
    r: bool = False
    i: int = 0
    while i < len(ls):
        r = r or (ls[i] == elem)
        i = i + 1
    return r


def buscar_v2(elem: int, ls: List[int]) -> bool:
    '''
    Requiere : nada .
    Devuelve : True sii elem aparece al menos una vez en ls.
    '''
    r: bool = False
    i: int = 0
    while i < len(ls) and not r:
        r = ls[i] == elem
        i = i + 1
    return r


def buscar_v2For(elem: int, ls: List[int]) -> bool:
    '''
    Requiere : nada .
    Devuelve : True sii elem aparece al menos una vez en ls.
    '''
    for entero in ls:
        if elem == entero:
            return True
    return False


def buscar_v1For(elem: int, ls: List[int]) -> bool:
    '''
    Requiere : nada .
    Devuelve : True sii elem aparece al menos una vez en ls.
    '''
    r: bool = False
    for entero in ls:
        r = r or (entero == elem)
    return r

# EJERCICIO 12 ---------------------------------------------------------------------------


def primera_ocurrencia(elem: int, ls: List[int]) -> int:
    '''
    Requiere : ls contiene al menos una ocurrencia de elem .
    Devuelve : el índice de la primera ocurrencia de elem en ls.
    '''
    i: int = 0
    while ls[i] != elem:
        i = i + 1
    return i

def primera_ocurrencia_for(elem: int, ls: List[int]) -> int:
    '''
    Requiere : ls contiene al menos una ocurrencia de elem .
    Devuelve : el índice de la primera ocurrencia de elem en ls.
    '''
    i: int = 0
    for entero in ls:
        if elem == entero:
            return i
        i += 1
    return i

def primera_ocurrencia_enumerate(elem: int, ls: List[int]) -> int:
    '''
    Requiere : ls contiene al menos una ocurrencia de elem .
    Devuelve : el índice de la primera ocurrencia de elem en ls.
    '''
    for (i,entero) in enumerate(ls,0):
        if elem == entero:
            return i
    return i



#EJERCICIO 13----------------------------------
''' 
Queda para repasar para el parcial.
'''
