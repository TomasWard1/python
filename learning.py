#tipos de datos en pyhton
numeroEntero = int(5)
numeroEntero2 = int(-5)
numeroEntero3 = int(0)

numeroFloat = float(5.3)

frase = string('hola mundo')

#operaciones
def valorAbsoluto(numero):
    abs(numero)

#funciones
def estamosEnClase(enClase:bool):
    if enClase== True:
        return'Estamos en clase'
    else:
        return 'No estamos en clase'

def promedioPonderado(TP1:int,P1:int,TP2:int,P2:int) -> int:
    return TP1 * 0.2 + TP1 * 0.2 + TP1 * 0.2 + TP1 * 0.2

#RunTIME
