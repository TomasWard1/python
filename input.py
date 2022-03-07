from ast import List


estadosBuenos:List = ['bien']
estadosMalos:List = ['mal']
estadosNormales:List = ['normal']

def robot():
    nombre = input('Como te llamas?\n')
    print('hola {}'.format(nombre))
    estado = input('Como estas hoy?\n')
    for estadoEnLista in estadosBuenos:
        if (estado.__contains__(estadoEnLista)):
            print('Que bueno que estas bien!')
        else:
            for estadoEnLista in estadosMalos:
                if (estado.__contains__(estadoEnLista) and (estado != 'normal') ):
                    print('Que fiaca que estas mal!')
                else:
                     for estadoEnLista in estadosNormales:
                        if (estado.__contains__(estadoEnLista)):
                            print('Hmm, como podriamos mejorar tu dia?')
                        else:
                            tipoDeEstado = input('No reconozco este estado. Es bueno, malo, o normal (responder con b,m,n)?\n')
                            if tipoDeEstado == 'b':
                                estadosBuenos.append(estado)
                            elif tipoDeEstado == 'm':
                                estadosMalos.append(estado)
                            elif tipoDeEstado == 'n':
                                estadosNormales.append(estado)

robot()
