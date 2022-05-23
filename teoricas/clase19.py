from typing import Tuple, Set, Dict

from attr import s

# TUPLAS ---------------------------------------------------------
date: Tuple[int, str, int] = (1, 'mayo', 2003)
string: str = ''
for objeto in date:
    string += (' ' + str(objeto))
# print(string)

# CONJUNTOS ---------------------------------------------------------
animales_1: Set[str] = {'leon', 'gato', 'pato', 'pajaro'}
cosas_voladoras: Set[str] = {'avion', 'pajaro', 'frisbee'}

#print(animales_1 & cosas_voladoras)

list(animales_1)
animales_1.add('pajaro')
animales_1.add('perro')
# print(set(animales_1))


def caracteres(s: str) -> Set[str]:
    ''' 
    Requiere: nada.
    Devuelve: el conjunto de los caracteres que aparecen en s.
    Ejemplo: caracteres('bananas') → {'b', 'a', 'n', 's'}
    '''
    caracteres: Set[str] = set()
    for caracter in s:
        caracteres.add(caracter)
    return caracteres


def caracteres_en_comun(s: str, t: str) -> Set[str]:
    ''' Requiere: nada.
    Devuelve: el conjunto de los caracteres que aparecen
    tanto en s como en t.
    Ej: caracteres_en_comun('bananas', 'peras') → {'a', 's'}
    '''
    return caracteres(s) & caracteres(t)

# print(caracteres_en_comun('bananas','peras'))


# DICCIONARIOS ---------------------------------------------------------
def recitar(n: int) -> str:
    ''' 
    Requiere: n >= 0
    Devuelve: un string con la recitación de los dígitos de n,
    en minúsculas y separados por espacios en blanco.
    Ejemplos: recitar(1234) --> 'uno dos tres cuatro'
    recitar(0)-->'cero'
    recitar(999)-->'nueve nueve nueve'
    '''
    numerosRecitados: Dict[str, str] = {
        '0':'cero',
        '1': 'uno',
        '2': 'dos',
        '3': 'tres',
        '4': 'cuatro',
        '5': 'cinco',
        '6': 'seis',
        '7': 'siete',
        '8': 'ocho',
        '9': 'nueve',
    }
    recitacion:str = ''
    for numero in str(n):
        recitacion += (numerosRecitados[numero] + ' ')
    return recitacion
