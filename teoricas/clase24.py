import turtle as t
t.shape('turtle')


def triangulo(d: float):
    ''' Dibuja un triángulo equilátero de lado d. '''
    t.forward(d)
    t.right(120)
    t.forward(d)
    t.right(120)
    t.forward(d)


def lineas_punteadas(n: int, d: float):
    ''' Dibuja n líneas punteadas de longitud d. '''
    for i in range(n):
        t.pendown()
        t.forward(d)  # dibujo
        t.penup()
        t.forward(d)  # no dibujo


def cuadrado(d: float):
    ''' Dibuja un cuadrado de lado d. Requiere: d>0'''
    t.forward(d)
    t.left(90)
    t.forward(d)
    t.left(90)
    t.forward(d)
    t.left(90)
    t.forward(d)
    t.left(90)


def montaña(d: float):
    t.forward(d/3)
    t.left(60)
    t.forward(d/3)
    t.right(120)
    t.forward(d/3)
    t.left(60)
    t.forward(d/3)


def escalera(n: int, d: int):
    if n == 0:
        return
    else:
        t.forward(d),
        t.left(90)
        t.forward(d)
        t.right(90)
        return escalera(n-1, d)


def escalera2(d: float, k: float):
    if d < 0:
        return
    else:
        escalera(1, d)
        return escalera2(d-k, k)


def espiral_cuadrada(d: int):
    if d == 0:
        return
    else:
        t.forward(d+5)
        t.left(90)
        t.forward(d+5)
        t.left(90)
        t.forward(d)
        t.left(90)
        t.forward(d)
        t.left(90)
        return espiral_cuadrada(d-10)


def montaña_recursiva(d: float, nivel: int):
    if nivel == 0:  # caso base
        t.forward(d)
    else:
        montaña_recursiva(d/3, nivel-1)
        t.left(60)
        montaña_recursiva(d/3, nivel-1)
        t.right(120)
        montaña_recursiva(d/3, nivel-1)
        t.left(60)
        montaña_recursiva(d/3, nivel-1)

t.speed(0)
escalera2(20,3)


t.mainloop()  # Siempre incluir estas dos operaciones
t.bye()
