import unittest

ORIGINYEAR:int = 1980

#Funcion para calcular el año bisiesto
def IsLeapYear(a:int) -> bool:
    ''' 
    Requiere : a >=0
    Devuelve : True si a es un año bisiesto ; False si no.
    '''
    b:bool = (a%4 == 0 and a%100 != 0) or (a%400 == 0)
    return b


def getCurrentYear(days:int) -> int:
    '''
    Requiere: la cantidad de dias desde 1980 (int)
    Devuelve: la cantidad de años que pasaron (int)
    '''
    counter:int = 0
    year:int = ORIGINYEAR

    while counter < days:
        if IsLeapYear(year):
            counter += 366
            year += 1
        else:
            counter+= 365
            year += 1
    return year

    