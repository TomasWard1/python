import random
import turtle as t
from operator import imod
from typing import List

# EJERCICIO 1 ========================================================================================
'''
(a) pot2(n): Dado un entero n ≥ 0, calcular 2^n
. Ejemplos: pot2(0) → 1; pot2(7) → 128.
'''


def pot2(n: int) -> int:
    '''
    Requiere: n ≥ 0
    Devuelve: 2^n 
    '''
    if n == 0:
        return 1
    else:
        return pot2(n-1) * 2


'''
(b) pot_a(a, n): Dados dos enteros n ≥ 0 y a, calcular a^n
. Ejemplos: pot_a(3, 0) → 1; pot_a(-2,7) → -128. Además, en particular pot_a(0, 0) debe devolver 1.
'''


def pot_a(a: int, n: int) -> int:
    '''
    Requiere: n ≥ 0
    Devuelve: a^n
    '''
    if n == 0:
        return 1
    else:
        return pot_a(a, n-1) * a


'''
(c) producto(n, m): Dados dos enteros n ≥ 0, m ≥ 0, calcular n * m. Sugerencia: hacer la recursión sobre el parámetro n, dejando fijo el valor de m.
'''


def producto(n: int, m: int) -> int:
    '''
    Requiere: n ≥ 0, m ≥ 0
    Devuelve: n * m
    '''
    if n == 1:
        return m
    else:
        return producto(n-1, m) + m


'''
(d) es_par(n): Determinar si un entero n ≥ 0 es par (o sea, debe devolver True si es par y
False en caso contrario). Sugerencia: pensar cómo podría ayudar restarle 2 a n.
'''


def es_par(n: int) -> bool:
    '''
    Requiere: n ≥ 0
    Devuelve: True si es par y False en caso contrario
    '''
    if n == 0:
        return True
    if n == 1:
        return False
    else:
        return es_par(n-2)


# EJERCICIO 2 ========================================================================================
'''
(a) productoria(xs): Dada una lista no vacía de enteros xs, calcular el resultado de multiplicar
todos los números de xs.
'''


def productoria(xs: List[int]) -> int:
    '''
    Requiere: lista no vacía
    Devuelve: el resultado de multiplicar todos los números de xs.
    '''
    if len(xs) == 1:
        return xs[0]
    else:
        return productoria(xs[1:]) * xs[0]


'''
(b) cantidad_ocurrencias(x, xs): Dada una lista de enteros xs y un entero x, devolver la
cantidad de veces que aparece x en xs.
'''


def cantidad_ocurrencias(x: int, xs: List[int]) -> int:
    '''
    Requiere: nada
    Devuelve: la cantidad de veces que aparece x en xs.
    '''
    if xs == []:
        return 0
    elif len(xs) == 1:
        if xs[0] == x:
            return 1
        else:
            return 0
    else:
        if xs[0] == x:
            return cantidad_ocurrencias(x, xs[1:]) + 1
        else:
            return cantidad_ocurrencias(x, xs[1:])


'''
(c) max_pos(xs): Dada una lista no vacía de enteros xs, devolver la posición del elemento más
grande. En caso de empate, devolver la posición de la primera aparición.
'''


def max_pos(xs: List[int]) -> int:
    '''
    Requiere: xs no vacia
    Devuelve: la posición del elemento más grande. En caso de empate, la posición de la primera aparición.
    '''
    if len(xs) == 1:
        return 0
    else:
        max_i: int = max_pos(xs[:-1])
        if xs[max_i] > xs[-1]:
            return max_i
        else:
            return len(xs)-1


'''
(d) contar_coincidencias(xs): Dada una lista de enteros xs, contar cuántas veces es cierto
que la i-ésima posición tiene el número i (es decir, cuántas veces xs[i]==i).
'''


def contar_coincidencias(xs: List[int]) -> int:
    '''
    Requiere: nada
    Devuelve: la cantidad de veces que xs[i]==i
    '''
    if xs == []:
        return 0
    elif len(xs) == 1:
        if xs[0] == 0:
            return 1
        else:
            return 0
    else:
        ultimo_i: int = len(xs)-1
        if xs[ultimo_i] == ultimo_i:
            return contar_coincidencias(xs[:-1]) + 1
        else:
            return contar_coincidencias(xs[:-1])


'''
(e) sumar_posiciones_pares(xs): Dada una lista de enteros, sumar los elementos en sus posiciones pares.
Ejemplo: sumar_posiciones_pares([1,2,9,4,3]) devuelve 13 = 1 + 9 + 3.
'''


def sumar_posiciones_pares(xs: List[int]) -> int:
    '''
    Requiere: nada
    Devuelve: la suma de los elementos en posiciones pares de xs
    '''
    if xs == []:
        return 0
    elif len(xs) == 1:
        print(xs)
        return xs[0]
    else:
        print(xs)
        if len(xs) % 2 == 0:
            return sumar_posiciones_pares(xs[1:])
        else:
            return sumar_posiciones_pares(xs[1:]) + xs[0]


# EJERCICIO 3 ========================================================================================
'''
(a) Escribir una función recursiva fibonacci(n) que dado un entero n ≥ 0, devuelva el término F-sub(n) de la sucesión de Fibonacci.
'''

i: int = 0


def fibonacci(n: int) -> int:
    global i
    i += 1
    print(f'fib called {i} times')
    '''
    Requiere: n ≥ 0
    Devuelve: el término F-sub(n) de la sucesión de Fibonacci.
    '''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)


'''
(b) Ejecutar fibonacci(50). ¿Por qué tarda tanto? (Probablemente sea necesario cortar la ejecución después de un tiempo.) Para buscar una respuesta (informal), hacer un seguimiento
de la evaluación de un ejemplo chico, como fibonacci(6).

Tarda tanto porque hay una doble recursion. Entonces por cada recursion se haran 2 mas, etc.
- sumar_posiciones_pares([1,2,3,4,5,6]) llama a la funcion 6 veces
- fibonacci(6) la llama 25 veces
'''

# EJERCICIO 4 ========================================================================================
t.shape('turtle')
t.clearscreen()
t.speed(0)

'''
(a) Definir una función iterativa iterativa que, dados d:float y n:int, dibuje un polígono regular con
n lados de longitud d. Por ejemplo, para n=5 y n=8:
'''


def poligono_regular(d: float, n: int):
    angulo_interior = 360/n

    while n != 0:
        t.forward(d)
        t.left(angulo_interior)
        n -= 1


'''
(b) Definir una función recursiva recursiva que, dados d:float, n:int e incr:float, dibuje una espiral
con n lados, comenzando con longitud d y reduciéndose en incr cada vez hasta llegar a 0.
'''


def espiral(d: float, n: int, incr: float):
    angulo_interior = 360/n

    if d == 0:
        pass
    else:
        t.forward(d+5)
        t.left(angulo_interior)
        return espiral(d-incr, n, incr)


def espiral_cuadrados_recursiva(d: float, n: int, incr: float, angulo: int):
    if d == 0:
        pass
    else:
        t.right(angulo+5)
        t.forward(d)
        t.left(90)
        t.forward(d)
        t.left(90)
        t.forward(d)
        t.left(90)
        t.forward(d)
        t.left(90)
        return espiral_cuadrados_recursiva(d-incr, n, incr, angulo)


# EJERCICIO 5 ========================================================================================
def arbol(altura: float, nivel: int):
    t.pencolor('brown')
    t.pensize(3)
    t.forward(altura)
    if nivel > 0 and altura > 1:
        t.pencolor('green')
        angulo:int = random.uniform(15,30)
        t.left(angulo)
        arbol(altura/2, nivel-1)
        t.right(2*angulo)
        arbol(altura/2, nivel-1)
        t.left(angulo)
        arbol(altura/2, nivel-1)
    t.backward(altura)

'''
(a) Ejecutar a mano arbol(100,0), arbol(100,1) y arbol(100,2), suponiendo que se empieza
en cada caso con la tortuga apuntando hacia arriba.
'''
t.setheading(90)
#arbol(100,0)
#arbol(100,1)
#arbol(100,2)

'''
(c) ¿En qué consiste el caso base en esta función recursiva?
El caso base de esta funcion consiste en que el nivel sea menor o igual a 0. En ese caso ir hacia adelante.
'''

'''
(d) Ejecutar arbol(100,8). Para acelerar la ejecución, reemplazar la línea 4 por if nivel>0
and altura>1:, así la tortuga no pierde el tiempo dibujando cosas imperceptibles. ¿Cómo
cambia la definición del caso base al hacer ese cambio?
Ahora el caso base tambien se ejectua si la altura es menor a 1.
'''
arbol(100,8)



t.mainloop()
t.bye()
