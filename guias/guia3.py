import unittest

#EJERCICIO 9 ------------------------------
def bisiesto (a:int) -> bool:
    ''' 
    Requiere : a >=0
    Devuelve : True si a es un año bisiesto ; False si no.
    '''
    b:bool = (a%4 == 0 and a%100 != 0) or (a%400 == 0)
    return b


class TestBisiesto(unittest.TestCase):
    def test_2020(self):
        a:int = 2020
        respuesta_funcion:bool = bisiesto(a)
        respuesta_esperada:bool = True
        self.assertEqual(respuesta_funcion, respuesta_esperada)

    def test_2021(self):
        a:int = 2021
        respuesta_funcion:bool = bisiesto(a)
        respuesta_esperada:bool = False
        self.assertEqual(respuesta_funcion, respuesta_esperada)

    def test_1900(self):
        a:int = 1900
        respuesta_funcion:bool = bisiesto(a)
        respuesta_esperada:bool = False
        self.assertEqual(respuesta_funcion, respuesta_esperada)

    def test_2000(self):
        a:int = 2000
        respuesta_funcion:bool = bisiesto(a)
        respuesta_esperada:bool = True
        self.assertEqual(respuesta_funcion, respuesta_esperada)

    def test_1(self):
        a:int = 1
        respuesta_funcion:bool = bisiesto(a)
        respuesta_esperada:bool = False
        self.assertEqual(respuesta_funcion, respuesta_esperada)
    
    def test_0(self):
        a:int = 0
        respuesta_funcion:bool = bisiesto(a)
        respuesta_esperada:bool = True
        self.assertEqual(respuesta_funcion, respuesta_esperada)

#EJERCICIO 10 ---------------------------------------
def controlar_m ( m1 :int , m2 : int) -> bool :
    ''' 
    Requiere : nada .
    Devuelve: True si los valores de m1 y m2 son seguros; False si no.
    '''
    ok : bool = False
    if m1 <70:
        ok = True
    return ok


print(controlar_m(2,2))


