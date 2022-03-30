import unittest

def sumar_digitos(s:str) -> int:
    '''
    Requiere: s esta formado solo por digitos (0123456789)
    Devuelve: la suma de los digitos de s
    '''
    i:int = 0
    suma:int = 0
    while i < len(s):
        digito:int = int(s[i])
        suma += digito
        i += 1
    return suma

class TestSumaDigitos(unittest.TestCase):
    def test1(self):
        s:str = '1234'
        resultado:int = sumar_digitos(s)
        esperado:int = 10
        self.assertEqual(resultado,esperado)

    def test_0(self):
        s:str = '0'
        resultado:int = sumar_digitos(s)
        esperado:int = 0
        self.assertEqual(resultado,esperado)

    def test_nulo(self):
        s:str = ''
        resultado:int = sumar_digitos(s)
        esperado:int = 0
        self.assertEqual(resultado,esperado)

    def test_4(self):
        s:str = '1000'
        resultado:int = sumar_digitos(s)
        esperado:int = 1
        self.assertEqual(resultado,esperado)


unittest.main()
