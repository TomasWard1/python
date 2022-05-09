from typing import List
import unittest
'''
Dados dos strings s y t, determinar si s es prefijo de t (es decir, determinar si t comienza con s).
Ejemplos: 'papa' es prefijo de 'papafrita', pero no de 'lapapa' ni de 'pap'.
Resolverlo con un ciclo, no con slices.
'''

def es_prefijo(prefijo: str, string: str) -> bool:
    if prefijo > string:
        return False

    for i, character in enumerate(prefijo):
        if character != string[i]:
            return False
    return True

def es_prefijo_while(prefijo: str, string: str) -> bool:
    if prefijo > string:
        return False

    i:int = 0
    #A
    while i < len(prefijo):
        #B


        
        if prefijo[i] != string[i]:
            return False
        i += 1
        #C
    #D
    return True

class TestPrefijo(unittest.TestCase):
    def test_true(self):
        self.assertEqual(es_prefijo_while('papa', 'papafrita'), True)
        self.assertEqual(es_prefijo_while('dino', 'dinosaurio'), True)
        self.assertEqual(es_prefijo_while('feli', 'feliroca'), True)
        self.assertEqual(es_prefijo_while('', ''), True)

    def test_false(self):
        self.assertEqual(es_prefijo_while('papa', 'firtpa'), False)
        self.assertEqual(es_prefijo_while('sau', 'dinosaurio'), False)
        self.assertEqual(es_prefijo_while('roc', 'r'), False)


unittest.main()
