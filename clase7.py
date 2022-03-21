def es_par (n:int) -> bool :
    ''' 
    Requiere: Nada.
    Devuelve: True si n es par , False si es impar.
    '''
    b : bool = ( n % 2 == 0)
    return b


def parImpar(x:int):
    if es_par(x):
        print('El numero es par')
    else:
        print('El numero es impar')

# i :int = 10
# while i >=1:
#     print ( i )
#     i = i - 1
# print ( ' despegue ! ')

#EJERCICIO 2 ------------------------------------------------------------------------------

p = False
q = True

if p:
    if q:
        print('A1')
    else:
        print('B1')

if p:
    if q:
        print('A2')
else:
    print('B2')

if p and q:
    print('A1')
elif p and not q:
    print('B1')

if p and q:
    print('A2')
elif not p or q:
    print('B2')

parImpar(2)