'''
Se tienen listas con los datos de personas que viven en localidades de la
provincia de Formosa. Cada persona se representa como una tripla
(Nombre, DNI, Edad) y en cada lista puede haber personas con el
mismo nombre.
Se desea tomar de a dos listas y obtener una lista de nombres ordenada
alfabéticamente y sin repetidos que cumpla con las siguientes
restricciones:
▶ Cada nombre aparece en ambas listas de personas.
▶ Cada nombre se corresponde con al menos una persona mayor de 80
años en cada lista.
'''

from typing import List, Tuple, Set, Dict

#################
## Ejercicio 1 ##
#################


def nombres_personas_mayores(personas: List[Tuple[str, int, int]], edad: int) -> Set[str]:
    res: Set[str] = set()

    for persona in personas:
        nombre: str = persona[0]
        edad: int = persona[2]
        if edad > 80:
            res.add(nombre)

    return res


def nombres_en_comun_personas_mayores(unas_personas: List[Tuple[str, int, int]], otras_personas: List[Tuple[str, int, int]]) -> List[str]:
    set_1: Set[str] = nombres_personas_mayores(unas_personas, 80)
    set_2: Set[str] = nombres_personas_mayores(otras_personas, 80)
    lista_ordenada: List[str] = sorted(list(set_1 & set_2))

    return lista_ordenada


# Para corroborar

clorinda: List[Tuple[str, int, int]] = [
    ("Dorotea", 14581, 82), ("Azucena", 27652, 75), ("Dorotea", 3245, 89), ("Felisberto", 987, 90)]
pirane: List[Tuple[str, int, int]] = [
    ("Azucena", 8613, 87), ("Dorotea", 5821, 88), ("Felisberto", 2854, 89), ("Luis", 99899, 35)]
mosconi: List[Tuple[str, int, int]] = [
    ("Dorotea", 42939, 67), ("Luis", 1150, 90)]

print(nombres_en_comun_personas_mayores(clorinda, pirane))
print(nombres_en_comun_personas_mayores(clorinda, mosconi))
print(nombres_en_comun_personas_mayores(pirane, mosconi))
print()


#################
## Ejercicio 2 ##
#################

def filtrarDict(dic: Dict[int, List[Tuple[str, int]]], dnis: List[str]) -> Dict[int, List[Tuple[str, int]]]:
    for key in dnis:
        if len(dic[key]) == 1:
            dic.pop(key)
    return dic


def dnis_mellizos(personas: List[Tuple[str, int, int]]) -> Dict[int, List[Tuple[str, int]]]:
    res: Dict[int, List[Tuple[str, int]]] = {}
    dnis: List[str] = []

    for persona in personas:
        dni: int = persona[1]
        valor_nuevo: Tuple[str, int] = (persona[0], persona[2])
        if dni in res:
            current_name: Tuple[str, int] = res[dni][0][0]
            current_age: Tuple[str, int] = res[dni][0][1]
            valor_viejo: Tuple[str, int] = (current_name, current_age)
            res[dni] = [valor_viejo, valor_nuevo]
        else:
            res[dni] = [valor_nuevo]
        dnis.append(dni)
        
    return filtrarDict(res, dnis)


# Para corroborar

personas: List[Tuple[str, int, int]] = [("Maria", 123456, 25),
                                        ("Ahmed", 6841635, 81),
                                        ("Jairo", 123456, 65),
                                        ("Matias", 35512, 90),
                                        ("Tomas", 355120, 8),
                                        ("Matias", 35512, 48)]

print(dnis_mellizos(personas))
