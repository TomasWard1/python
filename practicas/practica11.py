from typing import List
import unittest

lista_abcdef: List[str] = ['alta', 'altura',
                           'bandida', 'coqueta', 'dinamita', 'expensiva', ]


def esta_en(string: str, lista: List[str]) -> bool:
    '''
    Requiere una lista ordenada de strings de menor a mayor
    '''
    inicio: int = 0
    fin: int = len(lista)
    while inicio < fin:
        medio: int = (inicio + fin)//2
        if lista[medio] == string:
            return True
        elif lista[medio] < string:
            inicio = medio + 1
        else:
            fin = medio
    return False


class Test(unittest.TestCase):
    def testAPasar(self):
        self.assertTrue(esta_en('coqueta', lista_abcdef))
        self.assertFalse(esta_en('guapa', lista_abcdef))
        self.assertFalse(esta_en('racineta', lista_abcdef))

def padrones_donde_vota(padrones: List[List[str]], nombre: str) -> List[int]:
    """Devuelve los índices de los padrones en donde vota alguien de nombre "nombre"
    Requiere: Para todo i, 0 <= i < len(padrones), padrones[i] está ordenado alfabéticamente
    Devuelve: Para cada elemento e de vr, vale que padrones[e] contiene el nombre "nombre"
    """
    indices_encontrados: List[int] = []
    for i,padron in enumerate(padrones):
         encontramos:bool = esta_en(nombre, padron)
         if encontramos:
            indices_encontrados.append(i)

    return indices_encontrados

nombre1:str = 'Smith Alice'
nombre2:str = 'Smith Lee'

padrones: List[List[str]] = [['Smith Alice', 'Smith Bob'],['Smith Carl', 'Smith Lee'],['Smith Alice', 'Smith Carl']]

class TestPadron(unittest.TestCase):
    def testAPasar(self):
        self.assertEqual(padrones_donde_vota(padrones, nombre1), [0, 2])
        self.assertEqual(padrones_donde_vota(padrones, 'Smith Lee'), [1])

unittest.main()