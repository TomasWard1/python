def obtener_clima(temp:int) -> str:
  '''
  Requiere: 126 > temp > -273
  Devuelve: el clima del día para ser usado por el bot, donde segun el valor ingresado:
            - si es menor o igual a 10, devolver 'frio'
            - si se encuentra entre 10 y 17 grados, devolver 'templado'
            - si se encuentra entre 17 y 25 grados (inclusive), devolver 'agradable'
            - si es mayor a 25, devolver 'caluroso'
  '''
  frio:bool = temp <= 10
  templado:bool = 10 < temp < 17
  agradable:bool = 17 < temp <= 25
  caluroso:bool = temp > 25

  if -273 < temp < 126:
    if frio:
      return 'frio'
    elif templado:
      return 'templado'
    elif agradable:
      return 'agradable'
    elif caluroso:
      return 'caluroso'
  else:
    return 'La temperatura no esta en el rango'

