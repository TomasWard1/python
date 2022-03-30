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

# 1. Podríamos poner cualquier antidad de días.
# 2. El while loop solo suma años y va restando dias si los dias restantes son mayores a 365
# 3. Ejemplo: Si pones que pasaron 366 dias se forma un loop infinito.
# 4. Sigamos la logica:
# 5. La condicion del while loop es true
# 6. El año 1980 es bisiesto entonces chequea si dias > 366 que es falso
# 7. No suma años, ni resta dias, entonces ahi termina el bloque de while -> Comienza denuevo
# 8. Se genera un loop infinito
# RESUMEN: El error de microsoft es que si al estar restando dias, en algun punto te quedan 366, ocurre un loop infinito.
# SOLUCION: cambiar if days > 366 a if days >= 366

def CalculateCurrentYearError(days:int) -> int:
    ''' Requiere : days >= 0 , la cantidad de días transcurridos
    desde el 1 de enero de ORIGINYEAR.
    Devuelve : El año actual (ej: 2007). 
    '''
    year:int = ORIGINYEAR
    while days > 365:
        if IsLeapYear(year):
            #error: if days > 366
            #corregido:
            if days >= 366:
                days = days - 366
                year = year + 1
        else:
            days = days - 365
            year = year + 1
    return year

print(CalculateCurrentYearError(731))