#Ejercicio 1a
from re import I
import math


def f(x:int) -> int:
    x = x + 1
    return x

# x:int = 10
# print(f(x)) #imprime 11
# print(x) #imprime 10
# print(f(x*x)) #imprime 101
# print(x) #imprime 10

#Ejercicio 1b
def f ( x :int , y : int ) -> int :
    x = 2 * x + y
    return x

# x : int = 3
# y : int = 7
# y = f(y,x) #17
# x = f(y,x) #37
# print (x , y ) #37,17
# print (x , x * x ) #37, 1369 

#ejercicio 2
def f2c(f:float) -> float:
    c = (f - 32)*(5/9)
    return c 

# print(f2c(195))


#Ejercicio 3
def combinatorio(n:int,k:int) -> int:
    if n >= 0 and k >= 0 and k <= n:
        nFactorial:int = math.factorial(n)
        kFactorial:int = math.factorial(k)
        differenciaFactorial:int = math.factorial(n-k)
    
        combinatorio:int = nFactorial/(kFactorial*differenciaFactorial)
        print('El combinatorio nCk es {}'.format(int(combinatorio)))
    else:
        print('no se puede calcular el combinatorio')


def parteEnteraRaiz(n:int) -> int:
    """
    Requiere un numero entero mayor que 0, hace la raiz cuadrada y python lo redondea a int.

    """
    if n>0 or n==0:
        parteEntera = int(math.sqrt(n))
        math.fac
        return parteEntera
    else:
        print('Ingresar un numero mayor o igual a 0')
# print(parteEnteraRaiz(6))

#Ejercicio 4
def f ( s : str ) -> str :
    if s[0]== 'A' and len (s) > 0: 
        return ' Eureka '
    else:
        return ' Me aburro'

print(f(''))


