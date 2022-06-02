# Clases y Objetos - dou

from typing import Set, List


class Fruta:  # Definición de la clase Fruta. Typehints de la misma clase no funcionan.

    # init de la clase
    def __init__(self, n: str, p: float, es: Set[str]):
        ''' Inicializa una fruta con nombre n, precio p, estaciones es. '''
        self.nombre: str = n
        self.precio: float = p
        self.estaciones: Set[str] = es

    # funciones customizadas
    def disponible_en(self, estacion: str) -> bool:
        ''' Determina si esta fruta suele estar disponible en la estación dada.
        Requiere : estacion es 'primavera', 'verano', 'otoño' o 'invierno'.
        Devuelve : True si estacion está en las estaciones de la fruta;
        False en caso contrario.'''
        return estacion in self.estaciones

    #podes aplicar el 'less than' para darle semantica a la comparacion de objetos.
    def __lt__(self, other) -> bool:
        ''' Devuelve True si self < other; False en caso contrario.'''
        return self.precio < other.precio
        
    # como imprimir el objeto.

    def __repr__(self) -> str:
        ''' Devuelve una representación string de la fruta. '''
        return self.nombre + '($' + str(self.precio) + '/kg)'


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
PRI: str = 'primavera'
VER: str = 'verano'
OTO: str = 'otoño'
INV: str = 'invierno'

# Creación de 3 objetos de la clase Fruta.
p: Fruta = Fruta('Pera Williams', 70.0, {VER})
u: Fruta = Fruta('Uva verde', 60.0, {VER})
b: Fruta = Fruta('Banana de Ecuador', 150.0, {PRI, OTO, INV})

frutas: List[Fruta] = [b, p, u]

print(frutas[0])
