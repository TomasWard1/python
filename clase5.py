from ast import List
import math
from re import T

def volumen_cilindro(r:float, h:float) -> float:
    '''
    Requiere r,h > 0
    Devuelve: pi * rˆ2 * h
    '''
    if r > 0 and h > 0:
        pi:float = math.pi
        rSquared:float = r*r
        volumen = round(pi*rSquared*h,3)
        print('El volumen del cilindro es {}\n\n\n\n\n'.format(volumen))
    else:
        print('La altura y el radio tienen que ser positivos. Intentá denuevo')

#RUNTIME -----------------------
# radio = input('\n\n\n\n\nRadio:')
# altura = input('Altura:')

# try:
#     volumen_cilindro(float(radio),float(altura))
# except:
#     print('Ocurrio un error. Asegurate que estas pasando números.')

def stringPermitido(texto:str) -> bool:
    caracteresPermitidosMinusculas:str = ',.;:¿?¡!-"aábcdeéfghiíjklmnñoópqrstuúüvwxyz'
    caracteresPermitidosMayusculas:str = caracteresPermitidosMinusculas.upper()
    caracteresPermitidos:str = caracteresPermitidosMinusculas + caracteresPermitidosMayusculas
    aparecioProhibido:bool = False
    print(caracteresPermitidos)

    for caracter in texto:
        for permitido in caracteresPermitidos:
            if caracter == permitido:
               aparecioProhibido = True
            else: 
                aparecioProhibido = False
    
    return not aparecioProhibido
                


def contarVocales(texto:str) -> int:
    if stringPermitido(texto):
        vocalesMinusculas:str = 'aáeéiíoóuúü'
        vocalesMayusculas:str = vocalesMinusculas.upper() 
        vocales:str = vocalesMayusculas + vocalesMinusculas
        counter:int = 0

        for caracter in texto:
            for vocal in vocales:
                if caracter == vocal:
                    counter +=1

        return counter
    else:
        print('Error, string no permitido')

#no funciona el chequeo
print(contarVocales('abcdj)a'))