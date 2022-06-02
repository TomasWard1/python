from typing import Dict, TextIO, Set, List
import csv
from clase20 import Fruta

# unittesting de la clase
import unittest
from clase20 import Fruta

PRI: str = 'primavera'
VER: str = 'verano'
OTO: str = 'otoño'
INV: str = 'invierno'


class TestFruta(unittest.TestCase):
    def test_disponible_en(self):
        f1: Fruta = Fruta('Banana de Ecuador', 150.0, {PRI, OTO, INV})
        self . assertTrue(f1 . disponible_en(PRI))
        self . assertFalse(f1 . disponible_en(VER))
        self . assertTrue(f1 . disponible_en(OTO))
        self . assertTrue(f1 . disponible_en(INV))

        f2: Fruta = Fruta('Pera Williams', 70.0, {VER})
        self . assertFalse(f2 . disponible_en(PRI))
        self . assertTrue(f2 . disponible_en(VER))
        self . assertFalse(f2 . disponible_en(OTO))
        self . assertFalse(f2 . disponible_en(INV))

    def test_menor(self):
        f1: Fruta = Fruta('Banana de Ecuador', 150.0, {PRI, OTO, INV})
        f2: Fruta = Fruta('Pera Williams', 70.0, {VER})
        self . assertTrue(f2 < f1)
        self . assertFalse(f1 < f2)
        self . assertFalse(f1 < f1)
        self . assertFalse(f2 < f2)

    def test_repr(self):
        f1: Fruta = Fruta('Banana de Ecuador', 150.0, {PRI, OTO, INV})
        f2: Fruta = Fruta('Pera Williams', 70.0, {VER})
        self . assertEqual(str(f1), 'Banana de Ecuador($150.0/kg)')
        self . assertEqual(str(f2), 'Pera Williams($70.0/kg)')


# unittest.main()

class Catalogo:
    def __init__(self, archivo_csv: str):
        ''' Inicializa el catálogo de frutas , cargando las frutas contenidas en el archivo archivo_csv .
        Requiere : archivo_csv es el nombre de un archivo en formato
        CSV ( valores separados por comas ), con tres columnas :
        'nombre ' (str ), precio_por_kg ( float ), estaciones ( lista de
        strings separados por comas , donde los strings posibles son
        'primavera ', 'verano ', 'otoño ' o 'invierno ').
        '''
        self.frutas: List[Fruta] = []
        f: TextIO = open(archivo_csv)
        for linea in csv . DictReader(f):
            nombre: str = linea['nombre']
            precio: float = float(linea['precio_por_kg'])
            estaciones: Set[str] = set(linea['estaciones'].split(','))
            fru: Fruta = Fruta(nombre, precio, estaciones)
            self.frutas.append(fru)
        f.close()

    def frutas_de_estacion(self, estacion: str) -> List[Fruta]:
        '''
        Requiere : estacion es 'primavera ', 'verano ', 'otoño ' o 'invierno '
        Devuelve : las frutas disponibles en la estación dada (en algún orden ).
        '''
        vr: List[Fruta] = []
        for fru in self . frutas:
            if fru.disponible_en(estacion):
                vr.append(fru)
        return vr

    def __repr__(self) -> str:
        return str(self.frutas)


class Carrito:
    def __init__(self):
        ''' Inicializa un carrito vacío. Requiere: nada. '''
        self.kg_fruta: Dict[Fruta, int] = dict()

    def __repr__(self) -> str:
        ''' Devuelve un string con los datos del carrito. Requiere: nada. '''
        return str(self.kg_fruta)

    def agregar(self, f: Fruta, p: int):
        ''' Modifica: Agrega p kg de la fruta f al carrito. Requiere: p>0.'''
        if f in self.kg_fruta:
            self.kg_fruta[f] = self.kg_fruta[f] + p
        else:
            self.kg_fruta[f] = p

    def sacar(self, f: Fruta, p: int):
        ''' Modifica: Saca p kg de la fruta f del carrito.
        Requiere: p>0, y hay al menos p kilos de f. '''
        self.kg_fruta[f] = self.kg_fruta[f] - p
        if self.kg_fruta[f] == 0:
            self.kg_fruta. pop(f)

    def calcular_precio_total(self) -> float:
        ''' Devuelve: el precio total de la fruta en el carrito. Req: nada.'''
        vr: float = 0.0
        for fruta in self.kg_fruta:
            peso: int = self.kg_fruta
            vr = vr + peso*fruta.precio
        return vr

#un toque de testing.
carro:Carrito = Carrito()
catalogo:Catalogo = Catalogo('frutas.csv')
carro.agregar(catalogo.frutas[0],100)
carro.agregar(catalogo.frutas[0],4)
carro.agregar(catalogo.frutas[3],100)
carro.sacar(catalogo.frutas[0],100)

print(carro)