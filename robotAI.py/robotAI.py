from asyncio import sleep
from typing import List
from typing import TextIO

# VARIABLES----------------------------------------------------------------------------------
buenosFileHandlerR: TextIO = open('buenosEstados.txt')
malosFileHandlerR: TextIO = open('malosEstados.txt')
normalesFileHandlerR: TextIO = open('normalesEstados.txt')

buenosEstados: List[str] = buenosFileHandlerR.read().split('\n')
malosEstados: List[str] = malosFileHandlerR.read().split('\n')
normalesEstados: List[str] = normalesFileHandlerR.read().split('\n')

# FUNCIONES----------------------------------------------------------------------------------


def printSlow(string: str):
    for letter in string:
        print(letter, end='', flush=True)
        sleep(0.01)


def writeEstado(estado: str, type: str):
    buenosFileHandlerW: TextIO = open('buenosEstados.txt', 'w')
    malosFileHandlerW: TextIO = open('malosEstados.txt', 'w')
    normalesFileHandlerW: TextIO = open('normalesEstados.txt', 'w')

    match type:
        case 'b':
            buenosEstados.append(estado)
            buenosFileHandlerW.write('\n'.join(buenosEstados))
            buenosFileHandlerW.close()
        case 'm':
            malosEstados.append(estado)
            malosFileHandlerW.write('\n'.join(malosEstados))
            malosFileHandlerW.close()
        case 'n':
            normalesEstados.append(estado)
            normalesFileHandlerW.write('\n'.join(normalesEstados))
            normalesFileHandlerW.close()


writeEstado('meh', 'n')
writeEstado('bien', 'b')
print(normalesEstados)
print(buenosEstados)
