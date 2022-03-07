#ejercicio 1
from calendar import c
import operator

def corregir1(termino1,operador,termino2):
    print(operador(termino1,termino2))
    print(type(operador(termino1,termino2)))

#corregir1(str(123),operator.add,'123')

#ejercicio 8
import math

pi = round(math.pi,4)
e = round(math.e,4)

def escribirContantes():
    print('Pi rounded is: {}, e rounded is: {}'.format(pi,e))

#escribirContantes()


#ejercicio 10
def cambiarvariables():
    a:int = 10
    b:int = 20
    a = a+b #30
    b = a-b #30-20=10 (el valor de a)
    a = a-b #30-10=20 (el valor de b)
    print('Valor de M:{}, Valor de N:{}'.format(a,b))
    
#cambiarvariables()

#ejercicio 11
fahr:float = 80.0
cel:float = (fahr-32)*0.5556
#print('{} grados Farenheit equivalen a {} grados celcius'.format(fahr,cel))