# Ejercicio 1----------------------------------------------------------------------
from typing import List, TextIO
import random


def es_primo(n: int) -> bool:
    ''' 
    Requiere: n > 1, n sea numero natural.
    Devuelve: True si n es primo (es divisible unicamente por n y por 1)
    False en lo contrario.
    '''
    divisor: int = 2
    esPrimo: bool = True
    while divisor < n:
        if n % divisor == 0:
            esPrimo = False
        divisor += 1
    return esPrimo


def eslistaCreciente(lista: List[int]) -> bool:
    i: int = 0
    esEstrictamenteCreciente: bool = True

    while i < len(lista) - 1:
        numActual: int = lista[i]
        numProximo: int = lista[i+1]
        if numActual >= numProximo:
            esEstrictamenteCreciente = False
        i += 1

    return esEstrictamenteCreciente


def characters_in_lines(filename: str) -> List[int]:
    filehandler: TextIO = open(filename)
    listaCaracteres: List[int] = []

    for linea in filehandler:
        listaCaracteres.append(len(linea.rstrip()))

    return listaCaracteres


# Ejercicio 2----------------------------------------------------------------------
def new_file_characters_in_lines(filename: str, newFilename: str):
    filehandler: TextIO = open(filename)
    new_filehandler: TextIO = open(newFilename, 'w')
    listaCaracteres: List[int] = []

    for linea in filehandler:
        listaCaracteres.append(len(linea.rstrip()))

    for entero in listaCaracteres:
        new_filehandler.write(str(entero) + '\n')
    new_filehandler.close()


def file_n_primos(n: int, filename: str):
    '''
    Requiere que n>0
    '''
    primos_filehandler: TextIO = open(filename, 'w')
    primosCounter: int = 0
    numero: int = 2

    while primosCounter < n:
        if es_primo(numero):
            primos_filehandler.write(str(numero) + '\n')
            primosCounter += 1
        numero += 1
    primos_filehandler.close()

# Ejercicio 3----------------------------------------------------------------------


def filtrar_comentario(linea: str):
    linea_filtrada = ''
    for caracter in linea:
        if caracter != '#':
            linea_filtrada += caracter
        else:
            break
    return linea_filtrada


def filtrar_comentarios_file(fuente: str, destino: str):
    fuente_handler: TextIO = open(fuente)
    destino_handler: TextIO = open(destino, 'w')

    for linea in fuente_handler:
        destino_handler.write(filtrar_comentario(linea.rstrip()) + '\n')

    destino_handler.close()

# Ejercicio 4----------------------------------------------------------------------


def cuadrado_lado_n():
    n: int = int(input('Ingrese n:'))

    for i in range(n):
        print('*'*n)


def inversa_str():
    original: str = input('Ingrese un texto:')
    print(original[::-1])


def es_lista_creciente():
    lista: List[int] = input(
        "Ingrese una lista de enteros separados por comas:").split(',')
    res: str = ''
    for i, string in enumerate(lista):
        lista[i] = int(string)
    if eslistaCreciente(lista):
        res = 'La lista ingresada está ordenada en forma estrictamente creciente.'
    else:
        res = 'La lista ingresada no está ordenada en forma estrictamente creciente.'
    return res

# Ejercicio 5 ----------------------------------------------------------------------
def ejercicio5():
    print('A. Cuadrado')
    print('B. Inversa')
    print('C. Creciente')
    funcion:str = input('Que funcion del ejercicio 4 queres usar?').upper()

    if funcion == 'A':
        cuadrado_lado_n()
    elif funcion == 'B':
        inversa_str()
    elif funcion == 'C':
        es_lista_creciente()
    else:
        print('No se reconoce esta opcion. Proba denuevo.')

# Ejercicio 6 ----------------------------------------------------------------------
def practicar_multiplicacion():
    random1:int = random.randint(10,20)
    random2:int = random.randint(10,20)
    resultado_correcto:int = random1*random2
    resultado_usuario:int = int(input('Ingresar el resultado de {}*{}: '.format(random1,random2)))

    if resultado_correcto == resultado_usuario:
        print('Bien!')
    else:
        print('Mal! Resultado correcto: {}'.format(resultado_correcto))


