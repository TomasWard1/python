jugador1:str
jugador2:str
puntosJugador1:int = 0
puntosJugador2:int = 0

def registrar_jugadores():
    global jugador1
    global jugador2

    nombre1:str = input('Ingrese el nombre del primer jugador:')
    nombre2:str = input('Ingrese el nombre del segundo jugador:')

    jugador1 = nombre1
    jugador2 = nombre2

def puntaje_manual():
    global jugador1
    global jugador2
    global puntosJugador1
    global puntosJugador2

  
    ganadorPunto:str = input('Quién ganó este punto?')
    cuantoSumar(aQuienLeSumo=ganadorPunto)
    print(jugador1 + str(puntosJugador1) + "," + jugador2 + str(puntosJugador2))


def cuantoSumar(aQuienLeSumo:str) :
    global puntosJugador1
    global puntosJugador2
    
    if aQuienLeSumo == jugador1:
        #cada uno de los casos que pueden suceder al sumar puntos
        #los ponemos como variables porque se enitenden mas en el if.
        sumarNormal:bool = puntosJugador1 < 30
        sumarDiez:bool = puntosJugador1 == 30
        darVentaja:bool = puntosJugador1 == 40 and puntosJugador2 == 40
        darGame:bool = puntosJugador1 == 40 and not (puntosJugador2 == 40)
        darGameV2:bool = puntosJugador1 == 'ventaja' and puntosJugador2 == 40

        #chequear condiciones y sumar puntos
        if sumarDiez:
            puntosJugador1 += 10
        elif sumarNormal: 
            puntosJugador1 += 15
        elif darVentaja:
            puntosJugador1 = 'ventaja'
        elif darGame or darGameV2:
            puntosJugador1 = 'game'

    #hacer lo mismo para el segundo jugador
    elif aQuienLeSumo == jugador2:
        #cada uno de los casos que pueden suceder al sumar puntos
        sumarNormal:bool = puntosJugador2 < 30
        sumarDiez:bool = puntosJugador2 == 30
        darVentaja:bool = puntosJugador2 == 40 and puntosJugador1 == 40
        darGame:bool = puntosJugador2 == 40 and not (puntosJugador1 == 40)
        darGameV2:bool = puntosJugador2 == 'ventaja' and puntosJugador1 == 40

        #chequear condiciones y sumar puntos
        if sumarDiez:
            puntosJugador2 += 10
        elif sumarNormal: 
            puntosJugador2 += 15
        elif darVentaja:
            puntosJugador2 = 'ventaja'
        elif darGame or darGameV2:
            puntosJugador2 = 'game'

    else:
        print('No reconocemos a este jugador')

   
        

    

    


#PROGRAMA PRINCIPAL------
registrar_jugadores()

while puntosJugador1 != 'game' and puntosJugador2 != 'game':  
    puntaje_manual()


