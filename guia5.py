from typing import List
import unittest

#EJERCICIO 3 --------------------------------
def eslistaCreciente(lista:List[int]) -> bool:
    i:int = 0
    esEstrictamenteCreciente:bool = True

    while i < len(lista) - 1:
        numActual:int = lista[i]
        numProximo:int = lista[i+1]
        if numActual >= numProximo:
            esEstrictamenteCreciente = False
        i += 1

    return esEstrictamenteCreciente

class TestCreciente(unittest.TestCase):
    def test_estrictoCreciente(self):
        self.assertEqual(eslistaCreciente([1,2,3,4,5]),True)
        self.assertEqual(eslistaCreciente([5,7,8,19]),True)
        self.assertEqual(eslistaCreciente([100,101,102,103,104]),True)

    def test_creciente(self):
        self.assertEqual(eslistaCreciente([1,2,2,2,5]),False)
        self.assertEqual(eslistaCreciente([5,5,5,80,90]),False)
        self.assertEqual(eslistaCreciente([100,101,101,103,104]),False)

    def test_decrecienteEstricto(self):
        self.assertEqual(eslistaCreciente([6,5,4,3,2,1]),False)
        self.assertEqual(eslistaCreciente([90,80]),False)

    def test_decreciente(self):
        self.assertEqual(eslistaCreciente([6,5,5,5,2,1]),False)
        self.assertEqual(eslistaCreciente([5,5,5,3,2]),False)
        self.assertEqual(eslistaCreciente([100,100,99]),False)

    def test_cambio(self):
        self.assertEqual(eslistaCreciente([1,2,3,2]),False)
        self.assertEqual(eslistaCreciente([3,2,1,2,3]),False)

    def test_otros(self):
        self.assertEqual(eslistaCreciente([]),True)
        self.assertEqual(eslistaCreciente([5]),True)
        self.assertEqual(eslistaCreciente([100,100,100]),False)

def separarStringconSeparador(txt:str,sep:str):
    '''
    Requiere: len(sep) == 1
    Devuelve: Una nueva lista de str en donde cada elemento es la separacion de txt
    a partir de un separador sep.
    '''
    listaSeparada:List[str] = []

    i:int = 0
    entrada:str = ''
    print(listaSeparada, '#A', i)
    while i < len(txt):
        print(listaSeparada,'#B', i)
        if txt[i] != sep:
            entrada += txt[i]
        else:
            listaSeparada.append(entrada)
            entrada = ''
        i = i + 1
        print(listaSeparada, '#C', i)
    listaSeparada.append(entrada)
    print(listaSeparada, '#D', i)
    return listaSeparada

class TestSeparador(unittest.TestCase):
    def test_punto(self):
        self.assertEqual(separarStringconSeparador('a.b.c','.'),['a','b','c'])
    
    def test_coma(self):
        self.assertEqual(separarStringconSeparador('a,b,c',','),['a','b','c'])

    def test_separador_prePost(self):
        self.assertEqual(separarStringconSeparador(',a,b,c,',','),['','a','b','c',''])
        self.assertEqual(separarStringconSeparador('.a.b.c.','.'),['','a','b','c',''])


#Tomemos este caso como ejemplo
separarStringconSeparador('aaa,ajc,,b,c,dd',',')
'''
La consola imprime lo siguiente:
 #A
 #B
a #C
a #B
aa #C
aa #B
aaa #C
aaa #B
 #C
 #B
a #C
a #B
 #C
 #B
b #C
b #B
 #C
 #B
c #C
c #B
 #C
 #B
d #C
d #B
dd #C
dd #D
'''