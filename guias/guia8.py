import math
from typing import Dict, List, Set, Tuple
import unittest
# EJERCICIO 2 -------------------------------------------------------
'''
(a) Dado un punto en el plano (una tupla de dos floats), devolver su distancia al origen ((0.0,0.0)). Ejemplo: para el punto (4.0, 3.0), debe devolver 5.0.
'''

def hipotenusa(a: float, b: float) -> float:
    return math.sqrt(pow(a, 2) + pow(b, 2))


def distancia_origen(punto: Tuple[float, float]) -> float:
    return hipotenusa(punto[0], punto[1])


class TestDistancia(unittest.TestCase):
    def test_casos_regulares(self):
        self.assertAlmostEqual(distancia_origen((4.0, 3.0)), 5.0)
        self.assertAlmostEqual(distancia_origen((3.0, 3.0)), math.sqrt(18))

    def test_caso_zero(self):
        self.assertEqual(distancia_origen((0.0, 0.0)), 0.0)


'''
(b) Dados dos puntos en el plano, devolver su suma, componente a componente. Ejemplo: para los puntos (-1.0, 2.0) y (1.5, 3.3), debe devolver (0.5, 5.3).
'''


def suma_puntos(punto: Tuple[float, float], punto_2: Tuple[float, float]) -> Tuple[float, float]:
    return (punto[0]+punto_2[0], punto[1]+punto_2[1])


class SumaTesting(unittest.TestCase):
    def test_sumas(self):
        self.assertEqual(suma_puntos((4.0, 3.0), (4.0, 3.0)), (8.0, 6.0))
        self.assertEqual(suma_puntos((7.0, 3.0), (3.0, 7.0)), (10.0, 10.0))

    def test_zero(self):
        self.assertEqual(suma_puntos((0.0, 0.0), (0.0, 0.0)), (0.0, 0.0))


'''
(c) Dado un punto en el plano y un float f, devolver el punto resultante de sumar f a cada componente del punto. Ejemplo: para (-1.0, 2.0) y 3.3, debe devolver (2.3, 5.3).
'''
def sumar_a_componentes(punto: Tuple[float, float], f: float) -> Tuple[float, float]:
    return (punto[0]+f, punto[1]+f)


class SumaComponentesTesting(unittest.TestCase):
    def test_sumas(self):
        self.assertEqual(suma_puntos((4.0, 3.0), 2.0), (6.0, 5.0))
        self.assertEqual(suma_puntos((7.0, 3.0), 3.0), (10.0, 6.0))

    def test_zero(self):
        self.assertEqual(suma_puntos((0.0, 0.0), 0.0), (0.0, 0.0))


'''
(d) Dado un punto en el plano, devolver el punto entero más cercano. Ejemplo: para el punto (-1.9, 2.2), debe devolver (-2, 2). Sugerencia: usar round.
'''


def punto_mas_cercano(punto: Tuple[float, float]):
    return (round(punto[0]), round(punto[1]))


class SumaComponentesTesting(unittest.TestCase):
    def test_ejemplo(self):
        self.assertEqual(punto_mas_cercano((-1.9, 2.2)), (-2, 2))

    def test_zero(self):
        self.assertEqual(punto_mas_cercano((0.0, 0.0)), (0, 0))


# EJERCICIO 3 -------------------------------------------------------------------------------
def buscar(elem: int, lista: List[int]) -> Tuple[bool, int]:
    '''
    Requiere:nada.
    Devuelve:(True , p) si elem aparece en la lista por primera vez
    en la posición p; o bien (False , None ) si no aparece nunca.
    '''
    for p, elemento in enumerate(lista):
        if elemento == elem:
            return (True, p)
    return (False, None)

# EJERCICIO 5 -------------------------------------------------------------------------------


def strings_unicos(strings: List[str]) -> int:
    return len(set(strings))

# EJERCICIO 6 -------------------------------------------------------------------------------

def es_pangrama(texto: str) -> bool:
    abecedario: Set[str] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                            'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}

    return set(''.join(texto.split(' '))) == abecedario

# EJERCICIO 7 -------------------------------------------------------------------------------


def agregar1(x: str, c: Set[str]):
    c . add(x)


def agregar2(x: str, c: Set[str]) -> Set[str]:
    r = c | {x}
    return r


'''conjunto: Set[str] = set()
agregar1('a ', conjunto)
print(conjunto)

otro: Set[str] = conjunto
agregar1('b ', otro)
print(conjunto, otro)

otro = agregar2('c', otro)
print(conjunto, otro)

agregar1('d', conjunto)
print(conjunto, otro)
'''
# EJERCICIO 8 -------------------------------------------------------------------------------
def jaccard(A: Set[int], B: Set[int]) -> float:
    a_interseccion_b: Set[int] = A & B
    a_union_b: Set[int] = A | B
    return len(a_interseccion_b) / len(a_union_b)


def k_shingles(string: str, k: int) -> Set[str]:
    start: int = 0
    end: int = k

    res: Set[str] = set()
    ultimo_shingle_posible: str = string[len(string)-k:len(string)]

    while string[start:end] != ultimo_shingle_posible:
        shingle: str = string[start:end]
        res.add(shingle)
        start += 1
        end += 1

    res.add(ultimo_shingle_posible)
    return res


def plagio(string_1: str, string_2: str, k: int) -> float:
    k_shingles_1: Set[str] = k_shingles(string_1, k)
    k_shingles_2: Set[str] = k_shingles(string_2, k)
    return jaccard(k_shingles_1, k_shingles_2)

# EJERCICIO 9 -------------------------------------------------------------------------------


def apariciones_letras(string: str) -> Dict[str, int]:
    apariciones_dict: Dict[str:int] = {}
    for letter in string:
        if letter in apariciones_dict:
            apariciones_dict[letter] += 1
        else:
            apariciones_dict[letter] = 1
    return apariciones_dict

# El Ejercicio 10 me da toda la paja. Hay que hacer un diccionario con cada letra y su valor en deleetriado.

# EJERCICIO 11 -------------------------------------------------------------------------------


def construir_tabla(n: int) -> Dict[int, int]:
    ''' 
    Requiere: nada
    Devuelve: un diccionario con una llave int y su cuadrado como valor int.
    '''
    r: Dict[int, int] = dict()
    i: int = 1
    while i <= n:
        r[i] = i * i
        i = i + 1
    return r

# EJERCICIO 12 -------------------------------------------------------------------------------


def encontrar_max_valor(diccionario: Dict[str, int]) -> int:
    max: int = 0
    for key in diccionario:
        if diccionario[key] >= max:
            max = diccionario[key]
    return max


def valores_maximos(diccionario: Dict[str, int]) -> Set[str]:
    max: int = encontrar_max_valor(diccionario)
    res: Set[str] = set()
    for key in diccionario:
        if diccionario[key] == max:
            res.add(key)
    return res

# EJERCICIO 13 -------------------------------------------------------------------------------


def filtrar(tabla: Dict[int, int], digito: int):
    '''
    esta funcion filtra las entradas de un diccionario acorde al digito que tiene como parametro.
    Si digito = 0, cualquier valor del diccionario que tenga distinto ultimo digito sera eliminado.
    Requiere: digito sea natural.
    Modifica: tabla va a ser filtrada acorde al ultimo digito del valor de cada clave.
    Devuelve: nada 
    '''
    nuevo_dict:Dict[int,int] = dict(tabla)
    claves_a_eliminar: List[int] = []
    for k in nuevo_dict:
        valor:int = nuevo_dict[k]
        ultimo_digito:int = int(str(valor)[-1])
        if ultimo_digito != digito:
            claves_a_eliminar.append(k)
    for k in claves_a_eliminar:
        nuevo_dict.pop(k)

    return nuevo_dict

tabla:Dict[int, int] = construir_tabla(10)
otra: Dict[int, int] = tabla
print(otra) # {1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81,10:100}

filtrar(tabla, 9) # {3:9,7:49}
print(tabla) # {3:9,7:49}
print(otra) # {3:9,7:49}


