from ast import List, Str
from time import sleep


#VARIABLES
estadosBuenos:List = ['bien']
estadosMalos:List = ['mal']
estadosNormales:List = ['normal']

#FUNCIONES

def printSlow(string:str):
    for letter in string:
        print(letter,end='',flush=True)
        sleep(0.01)

def queDecirAPartirDeEstado(lista:List):
    if 'bien' in lista:
        printSlow('🤖 Que bueno que estas bien!')
    elif 'mal' in lista:
        printSlow('🤖 Que fiaca que estas mal!')
    elif 'normal' in lista:
        printSlow('🤖 Hace algo que te gusta asi te sentis bien!')

def agregarEstadoALista(donde:str, estado:str):
    if donde == 'b':
        estadosBuenos.append(estado)
    elif donde == 'n':
        estadosNormales.append(estado)
    elif donde == 'm':
        estadosMalos.append(estado)
    else:
        printSlow('🤖 Porfavor responder con las letras b,n,m')
        agregarEstadoALista(input('🤖 No Reconozco Este Estado. Es bueno, malo, o normal? Responder con: b,m,n\n'),estado)

def chequearEstadoEnListas(estado:str, listasDeEstados:List,enListas=False):
    lista:List = ['jiej']
    for lista in listasDeEstados:
        if estado in lista:
            queDecirAPartirDeEstado(lista)
            enListas = True
    if enListas == False:
      dondeAgregar = input('🤖 No Reconozco Este Estado. Es bueno, malo, o normal? Responder con: b,m,n\n')
      agregarEstadoALista(dondeAgregar,estado)

def robotInteligente(veces=1):
    while veces > 0:
        if veces == 1:
            nombre = input('🤖Como te llamas?\n')
            printSlow('🤖 Hola {}, un gusto.'.format(nombre))

        else:
            if veces >= 2:
                 printSlow('-----------\n🤖 Comenzemos de nuevo\n----------------')
        
        estado = input('🤖 Como estas hoy?\n')
        chequearEstadoEnListas(estado,[estadosBuenos,estadosMalos,estadosNormales],False)
        veces+=1


#RUN
robotInteligente(1)
