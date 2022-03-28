from operator import truediv


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

    if ganadorPunto == jugador1:
        if puntosJugador1 == 40 and puntosJugador2 == 40:
            puntosJugador1 = 'adv'
        elif puntosJugador1 == 30:
            puntosJugador1 += 10
        else:
            puntosJugador1 += 15
    elif ganadorPunto == jugador2:
        puntosJugador2 += 15
    else:
        print('No reconocemos a este jugador')
    
    print(jugador1 + str(puntosJugador1) + "," + jugador2 + str(puntosJugador2))



#PROGRAMA PRINCIPAL------
registrar_jugadores()

#suponemos que queres registrar 3 puntos seguidos

repetir:bool = True

while repetir == True:  
    puntaje_manual()


