import random
import math
from typing import List

# Ejercicio 1 ----------------------------------


class Punto:
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y

    def distancia_a(self, p) -> float:
        return math.sqrt(pow(p.x-self.x, 2) + pow(p.y-self.y, 2))

    def distancia_al_origen(self) -> float:
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def __add__(self, p):
        return Punto(self.x+p.x, self.y+p.y)

    def __eq__(self, p) -> bool:
        x_iguales: bool = self.x == p.x
        y_iguales: bool = self.y == p.y
        return x_iguales and y_iguales

    def __repr__(self) -> str:
        return '({},{})'.format(self.x, self.y)

#punto:Punto = Punto(1.23,-2.00)
#punto2:Punto = Punto(1,2)


# Ejercicio 2 ----------------------------------
class Dado:
    def __init__(self, caras: int):
        '''
        Requiere caras >=2
        '''
        self.caras: int = caras
        self.valor_actual: int = 0

    def tirar(self):
        numeros: List[int] = list(range(1, self.caras+1))
        numero_tirado = random.choice(numeros)
        self.valor_actual = numero_tirado
        return numero_tirado

    def __repr__(self) -> str:
        return str(self.valor_actual)

class CubileteDeGenerala:
    def __init__(self,dados:List[Dado]):
        self.dados:List[Dado]= dados

    def tirar_todos(self):
        for dado in self.dados:
            dado.tirar()
    
    def __repr__(self) -> str:
        valores:str = ''
        for dado in self.dados:
            valores += str(dado) + ' '
        return valores

def tirada(cubilete:CubileteDeGenerala):
    dados_a_tirar:List[str] = input('Cuales dados queres volver a tirar (1-5)? Ej: 3,4\n').split(',')

    if dados_a_tirar != ['']:
        for numero_dado in dados_a_tirar:
            cubilete.dados[int(numero_dado)-1].tirar()

def generala():
    print('\nBIENVENIDO A LA GENERALA')
    cubilete:CubileteDeGenerala = CubileteDeGenerala([Dado(6),Dado(6),Dado(6),Dado(6),Dado(6)])
    cubilete.tirar_todos()
    print('\nTiro 1: ' + str(cubilete))
    tirada(cubilete)
    print('\nTiro 2: ' + str(cubilete))
    tirada(cubilete)
    print('\n\nSu turno ha finalizado. Tus dados finales son {}\n\n'.format(cubilete))

while True:
    generala()
    