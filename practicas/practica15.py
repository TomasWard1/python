from typing import List


def factorial(n:int) -> int:
    if n == 1:
        return 1
    else:
        return factorial(n-1) * n

def suma_digitos(n:int) -> int:
    n_str:str = str(n)
    ultimo_digito:int = int(n_str[len(n_str)-1])
   
    if len(n_str) == 1:
        return int(n_str)
    else:
        todos_menos_ultimo:int = int(n_str[:len(n_str)-1])
        return suma_digitos(todos_menos_ultimo) + ultimo_digito

def suma_impares(n:int) -> int:
    if n == 1:
        return 1
    else:
        n_impar = (n*2) - 1 
        return suma_impares(n-1) + n_impar

def sumar_n(lista:List[int],i:int) -> List[int]:

    if len(lista) == 0:
        return lista
    else:
        lista[0] += i
        print(lista)
        return [lista[0]] + sumar_n(lista[1:],i)

def codificacion_inversa(lista:List[str]) ->str:
    if len(lista) == 1:
        return lista[0]
    else:
        return codificacion_inversa(lista[1:]) + lista[0]

print(codificacion_inversa(['mo','rit','go','al']))
print(codificacion_inversa(['as','tom','','rd',]))
