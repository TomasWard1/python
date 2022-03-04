#tipos de datos en pyhton joya
numeroEntero = int(5)
numeroEntero2 = int(-5) #numeros enteros (Z) pero son finitos por el limite de procesamiento de una computadora.
numeroEntero3 = int(0)

#operaciones
def valorAbsoluto(numero):
    abs(numero)

#funciones
def estamosEnClase(enClase:bool):
    if enClase== True:
        return'Estamos en clase'
    else:
        return 'No estamos en clase'

#PROMEDIO = TP1 * 0,2 + P1 * 0,2 + TP2 * 0,3 + P2 * 0,3
#debe ser mayor o igual a 60 para promocionar.

def promedioPonderado(TP1:int,P1:int,TP2:int,P2:int) -> int:
    return TP1 * 0.2 + TP1 * 0.2 + TP1 * 0.2 + TP1 * 0.2


#RunTIME
print(estamosEnClase(False))
print(valorAbsoluto(-5))