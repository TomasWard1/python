#EJERCICIO 1-------------
def f2c(f:float) -> float:
    c = (f - 32)*(5/9)
    return c 

def tablaF2C():
    f:int = 0
    tabla:str = ''

    while f <= 120:
        tableRow = '\n {} F = {} C'.format(str(f),str(round(f2c(f))))
        tabla = tabla + tableRow 
        f += 10
    print(tabla)


#EJERCICIO 2-------------
def es_polindromo(palabra:str):
    longitudP:int = len(palabra)
    polindromo:bool = True
    i:int = 0

    while i < longitudP:
        caracter:str = palabra[i]
        caracterOpuesto:str = palabra[longitudP-1-i]
        caracterIgual = (caracter == caracterOpuesto)

        chequeo:str = 'Es {} que {} y {} son iguales'.format(caracterIgual,caracter,caracterOpuesto)
        print(chequeo)

        polindromo = caracterIgual
        i += 1

    return polindromo

import unittest

class TestPolindromo(unittest.TestCase):
  def test_polindromo(self):
    palabra:str = 'reconocer'
    respuesta_func:bool = es_polindromo(palabra)
    respuesta_esperada:bool = True
    self.assertEqual(respuesta_func, respuesta_esperada)

  def test_no_polindromo(self):
    palabra:str = 'desconocer'
    respuesta_func:bool = es_polindromo(palabra)
    respuesta_esperada:bool = False
    self.assertEqual(respuesta_func, respuesta_esperada)

  def test_null(self):
    palabra:str = ''
    respuesta_func:bool = es_polindromo(palabra)
    respuesta_esperada:bool = True
    self.assertEqual(respuesta_func, respuesta_esperada)

  def test_space(self):
    palabra:str = ' '
    respuesta_func:bool = es_polindromo(palabra)
    respuesta_esperada:bool = True
    self.assertEqual(respuesta_func, respuesta_esperada)

  def test_letras(self):
    palabra:str = 'rrrrr'
    respuesta_func:bool = es_polindromo(palabra)
    respuesta_esperada:bool = True
    self.assertEqual(respuesta_func, respuesta_esperada)

unittest.main()