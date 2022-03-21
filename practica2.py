#ejercicio 1

def es_par(x:int) -> bool:
    '''
    Requiere: int
    Devuelve: bool
    x par: False
    x inpar: True
    '''
    rv:bool = (x+1)%2 == 0
    return rv

def es_par_bis(x:int) -> bool:
    '''
    Requiere: int
    Devuelve: bool
    x par: True
    x inpar: False
    '''
    rv:bool = x//2 - x/2 == 0
    return rv

import unittest

class testEsPar(unittest.TestCase):
    def test_par(self):
        self.assertEqual(es_par_bis(2),True)
        self.assertEqual(es_par(2),False)
        
    def test_inpar(self):
        self.assertEqual(es_par_bis(3),False)
        self.assertEqual(es_par(3),True)




