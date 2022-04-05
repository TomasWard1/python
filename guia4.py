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
def es_polindromo(palabra:str) -> bool:
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

from typing import List
import unittest

# class TestPolindromo(unittest.TestCase):
  # def test_polindromo(self):
  #   palabra:str = 'reconocer'
  #   respuesta_func:bool = es_polindromo(palabra)
  #   respuesta_esperada:bool = True
  #   self.assertEqual(respuesta_func, respuesta_esperada)

  # def test_no_polindromo(self):
  #   palabra:str = 'desconocer'
  #   respuesta_func:bool = es_polindromo(palabra)
  #   respuesta_esperada:bool = False
  #   self.assertEqual(respuesta_func, respuesta_esperada)

  # def test_null(self):
  #   palabra:str = ''
  #   respuesta_func:bool = es_polindromo(palabra)
  #   respuesta_esperada:bool = True
  #   self.assertEqual(respuesta_func, respuesta_esperada)

  # def test_space(self):
  #   palabra:str = ' '
  #   respuesta_func:bool = es_polindromo(palabra)
  #   respuesta_esperada:bool = True
  #   self.assertEqual(respuesta_func, respuesta_esperada)

  # def test_letras(self):
    # palabra:str = 'rrrrr'
    # respuesta_func:bool = es_polindromo(palabra)
    # respuesta_esperada:bool = True
    # self.assertEqual(respuesta_func, respuesta_esperada)


#EJERCICIO 3--------------
def es_primo(numero:int) -> bool:
  esPrimo:bool = True
  divisor:int = 2
  
  while divisor < numero: 
    resto:int = numero%divisor
    restoZero:bool = (resto == 0)
    if restoZero:
      esPrimo = False
    divisor += 1

  #el zero no es primo
  if numero == 0:
    esPrimo = False

  return esPrimo

class TestPrimo(unittest.TestCase):
  def test_primo(self):
    numero:int = 7
    respuesta_func:bool = es_primo(numero)
    respuesta_esperada:bool = True
    self.assertEqual(respuesta_func, respuesta_esperada)

  def test_no_primo(self):
    numero:int = 10
    respuesta_func:bool = es_primo(numero)
    respuesta_esperada:bool = False
    self.assertEqual(respuesta_func, respuesta_esperada)
  
  def test_zero(self):
    numero:int = 0
    respuesta_func:bool = es_primo(numero)
    respuesta_esperada:bool = False
    self.assertEqual(respuesta_func, respuesta_esperada)

  def test_cien(self):
    numero:int = 100
    respuesta_func:bool = es_primo(numero)
    respuesta_esperada:bool = False
    self.assertEqual(respuesta_func, respuesta_esperada)

  def test_primo_grande(self):
    numero:int = 13
    respuesta_func:bool = es_primo(numero)
    respuesta_esperada:bool = True
    self.assertEqual(respuesta_func, respuesta_esperada)


def es_prefijo (s:str,t:str) -> bool :
  '''
  Requiere : len(s) <= len(t)
  Devuelve : True si en toda posición j entre 0 y len(s) -1 ,
  s[j]==t[j]; False en caso contrario .
  '''
  aux:bool = True
  i:int = 0

  while i <len(s) and i <len(t) :
    aux = aux and s[i]==t[i]
    i = i + 1
  
  vr:bool = aux and i == len(s)
  return vr



