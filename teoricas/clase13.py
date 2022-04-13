import random
from typing import List, TextIO

provinciasFileHandler: TextIO = open(
    r'C:\Users\54911\Downloads\provincias.txt')
#textoProvincias:str = provinciasFileHandler.read()

for linea in provinciasFileHandler:
    linea = linea.rstrip().split('___')
    #print(linea[1])

#--------------------------------------------------------------------------------------
f: TextIO = open('mundiales.txt', 'w')

mundiales:List[str] = [' Corea - Japón ', ' Alemania ',' Sudáfrica ', ' Brasil ', ' Rusia ']

for m in mundiales:
    f.write(m + "\n")
f.close()

#--------------------------------------------------------------------------------------

adivino:bool = False
intentos:int = 0
n:int = random.randint(1,5)

while not adivino:
    intentos += 1
    respuesta:str = input('Adiviná en qué número del 1 al 5 estoy pensando:')
    if (int(respuesta)) == n:
        adivino = True
    else:
        print('Nop')

print('Bien, adivinaste en {} intentos'.format(intentos))
    

