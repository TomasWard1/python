def robot():
    nombre = input('Como te llamas?')
    print('hola {}'.format(nombre))
    estado = input('Como estas hoy?')
    if (estado.__contains__('bien')):
        print('Que bueno que estas bien!')
    else:
        print('Uyy, ojala estes mejor.')
    

robot()