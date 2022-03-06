#ejercicio 1
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

escribirContantes()
