from time import sleep
from naipes import Naipe, Mazo
import random
import math
from typing import List, Set, Tuple


def printSlow(string: str):
    for letter in string:
        print(letter, end='', flush=True)
        sleep(0.02)

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

    # def __eq__(self, p) -> bool:
    #     x_iguales: bool = self.x == p.x
    #     y_iguales: bool = self.y == p.y
    #     return x_iguales and y_iguales

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
    def __init__(self, dados: List[Dado]):
        self.dados: List[Dado] = dados

    def tirar_todos(self):
        for dado in self.dados:
            dado.tirar()

    def __repr__(self) -> str:
        valores: str = ''
        for dado in self.dados:
            valores += str(dado) + ' '
        return valores


def tirada(cubilete: CubileteDeGenerala):
    dados_a_tirar: List[str] = input(
        'Cuales dados queres volver a tirar (1-5)? Ej: 3,4\n').split(',')

    if dados_a_tirar != ['']:
        for numero_dado in dados_a_tirar:
            cubilete.dados[int(numero_dado)-1].tirar()


def generala():
    printSlow('\nBIENVENIDO A LA GENERALA')
    cubilete: CubileteDeGenerala = CubileteDeGenerala(
        [Dado(6), Dado(6), Dado(6), Dado(6), Dado(6)])
    cubilete.tirar_todos()
    printSlow('\nTiro 1: ' + str(cubilete))
    tirada(cubilete)
    printSlow('\nTiro 2: ' + str(cubilete))
    tirada(cubilete)
    printSlow(
        '\n\nSu turno ha finalizado. Tus dados finales son {}\n\n'.format(cubilete))

# while True:
#     generala()


# Ejercicio 3 ----------------------------------

mazo: Mazo = Mazo()
mazo.agregar(Naipe(7, 'oros'))
mazo.agregar(Naipe(1, 'espadas'))
mazo.agregar(Naipe(12, 'copas'))
mazo.agregar(Naipe(4, 'bastos'))
# print(mazo.naipe_mas_alto())

# EJERCICIO 4 ----------------------------------


class ConjuntoDePuntos:
    def __init__(self, puntos: Set[Punto]) -> None:
        self.puntos = puntos

    def centro_conjunto(self):
        cant_puntos: int = 0
        total_x: float = 0
        total_y: float = 0
        for punto in self.puntos:
            total_x += punto.x
            total_y += punto.y
            cant_puntos += 1
        return Punto(round(total_x/cant_puntos, 1), round(total_y/cant_puntos, 2))

    def agregar_punto(self, punto: Punto):
        self.puntos.add(punto)

    def __repr__(self) -> str:
        return str(self.puntos)


puntos: ConjuntoDePuntos = ConjuntoDePuntos(
    {Punto(1.0, 5.0), Punto(3.0, -5.0), Punto(0.5, 9.9)})

# print(puntos.centro_conjunto())

# EJERCICIO 5 ----------------------------------


class Tateti:
    def __init__(self) -> None:
        self.tablero: List[List[str]] = [
            [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.jugador1: Tuple[str, str] = ('Humano', 'X')
        self.jugador2: Tuple[str, str] = ('Bot', 'O')
        self.movimientos_j1: int = 0
        self.movimientos_j2: int = 0
        self.fila1: List[str] = self.tablero[0]
        self.fila2: List[str] = self.tablero[1]
        self.fila3: List[str] = self.tablero[2]

    def a_quien_le_toca(self) -> Tuple[str, str]:
        if self.movimientos_j1 < self.movimientos_j2:
            return self.jugador1
        elif self.movimientos_j1 > self.movimientos_j2:
            return self.jugador2
        return self.jugador1

    def lugar_esta_vacio(self, lugar: str):
        return lugar == ' '

    def indice_fila_elegida(self, posicion: int) -> int:
        if posicion <= 3:
            return 0
        elif 3 < posicion <= 6:
            return 1
        else:
            return 2

    def pedir_lugar_tablero(self, bot: bool) -> int:
        lugar_tablero: int = 0
        if bot:
            lugar_tablero = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])
            printSlow('\nEl bot eligio poner en ' + str(lugar_tablero))
        else:
            lugar_tablero = int(
                input('\nA donde queres poner?\n\n|1|2|3|\n|4|5|6|\n|7|8|9|\n'))
        return lugar_tablero

    def resta_necesaria(self, i_fila: int) -> int:
        if i_fila == 0:
            return 1
        elif i_fila == 1:
            return 4
        return 7

    def hacer_movimiento(self, jugador: Tuple[str, str], bot: bool):
        lugar_tablero: int = self.pedir_lugar_tablero(bot)
        i_fila: int = self.indice_fila_elegida(lugar_tablero)
        resta_necesaria: int = self.resta_necesaria(i_fila)
        
        # chequeamos que la posicion no este tomada, y le pedimos al bot o al usuario de elegir devuelta sino
        while not self.lugar_esta_vacio(self.tablero[i_fila][lugar_tablero-resta_necesaria]):
            print('\nEse lugar esta tomado, elegi devuelta')
            lugar_tablero = self.pedir_lugar_tablero(bot)
            i_fila = self.indice_fila_elegida(lugar_tablero)
            resta_necesaria = self.resta_necesaria(i_fila)

        i_fila = self.indice_fila_elegida(lugar_tablero)
        resta_necesaria = self.resta_necesaria(i_fila)
        self.tablero[i_fila][lugar_tablero-resta_necesaria] = jugador[1]

    def termino(self) -> bool:
        return self.ganador() != ''

    def gano_fila(self) -> Tuple[bool, str]:
        horiz1: bool = (self.fila1[0] == self.fila1[1] == self.fila1[2]) and  self.fila1[0] != ' '
        horiz2: bool = (self.fila2[0] == self.fila2[1] == self.fila2[2]) and  self.fila2[0] != ' '
        horiz3: bool = (self.fila3[0] == self.fila3[1] == self.fila3[2])  and  self.fila3[0] != ' '

        return (horiz1, self.fila1[0]) or (horiz2, self.fila2[0]) or (horiz3, self.fila3[0])

    def gano_columna(self) -> Tuple[bool, str]:
        col1: bool = (self.fila1[0] == self.fila2[0] == self.fila3[0]) and self.fila1[0] != ' '
        col2: bool = (self.fila1[1] == self.fila2[1] == self.fila3[1]) and self.fila1[1] != ' '
        col3: bool = (self.fila1[2] == self.fila2[2] == self.fila3[2]) and self.fila1[2] != ' '

        return (col1, self.fila1[0]) or (col2, self.fila1[1]) or (col3, self.fila1[2])

    def gano_diagonal(self) -> Tuple[bool, str]:
        diag1: bool = (self.fila1[0] == self.fila2[1] == self.fila3[2]) and self.fila1[0] != ' '
        diag2: bool = (self.fila3[0] == self.fila2[1] == self.fila1[2]) and self.fila3[0] != ' '

        return (diag1, self.fila1[0]) or (diag2, self.fila3[0])

    def ganador(self) -> str:
        gano_fila: bool = self.gano_fila()[0]
        gano_columna: bool = self.gano_columna()[0]
        gano_diag: bool = self.gano_diagonal()[0]

        if gano_fila:
            return self.gano_fila()[1]
        elif gano_columna:
            return self.gano_columna()[1]
        elif gano_diag:
            return self.gano_diagonal()[1]
        elif self.movimientos_j1 + self.movimientos_j2 == 9:
            return 'empate'
        else:
            return ''

    def movimiento_bot(self):
        self.hacer_movimiento(self.jugador2, bot=True)

    def __repr__(self) -> str:
        return f'\n|{self.fila1[0]}|{self.fila1[1]}|{self.fila1[2]}|\n|{self.fila2[0]}|{self.fila2[1]}|{self.fila2[2]}|\n|{self.fila3[0]}|{self.fila3[1]}|{self.fila3[2]}|\n'


def jugarTateti():
    tateti: Tateti = Tateti()
    printSlow('\n\nBIENVENIDO AL TATETI')

    while not tateti.termino():
        jugador_a_mover: Tuple[str, str] = tateti.a_quien_le_toca()
        if jugador_a_mover[0] == 'Humano':
            tateti.hacer_movimiento(jugador_a_mover, bot=False)
            tateti.movimientos_j1 += 1
        else:
            tateti.movimiento_bot()
            tateti.movimientos_j2 += 1
        print(tateti)

    ganador: str = tateti.ganador()

    if (ganador == 'empate'):
        printSlow('EMPATE')
    else:
        printSlow(f'\nFELICITACIONES "{ganador}", sos victorioso.')


while True:
    jugarTateti()
