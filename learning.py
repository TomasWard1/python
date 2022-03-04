#tipos de datos en pyhton
numeroEntero = int(5)
numeroEntero2 = int(-5)
numeroEntero3 = int(0)

numeroFloat = float(5.3)

frase = str('hola mundo')

#operaciones-
def valorAbsoluto(numero):
    abs(numero)

#funciones
def estamosEnClase(enClase):
    if enClase== True:
        return'Estamos en clase'
    else:
        return 'No estamos en clase'

def promedioPonderado(TP1,P1,TP2,P2):
     print(TP1 * 0.2 + TP1 * 0.2 + TP1 * 0.2 + TP1 * 0.2)

#RunTIME
promedioPonderado(5,4,10,3)