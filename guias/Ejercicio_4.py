from typing import List

lista_ejemplo: List[int] = [1, 1, 2, 6, 6, 6, 3, 3]


def a(l: List[int]) -> int:
    index: int = 1
    largest: int = 0

    while index < len(l):
        if l[index - 1] == l[index] and l[index] > largest:
            largest = l[index]
        index += 1

    return largest


print(a(lista_ejemplo))

def b(l: List[int]) -> List[List]:
    ls_mesetas: List[List] = []
    ls: List[int] = []
    last_number: int = l[0]
    index: int = 0

    while index < len(l):
        if l[index] == last_number:
            ls.append(l[index])
        else:
            ls_mesetas.append(ls)
            last_number = l[index]
            ls = [l[index]]

        index += 1
    ls_mesetas.append(ls)

    return ls_mesetas


print(b(lista_ejemplo))

def c(l: List[int]) -> List[int]:
    index: int = 0
    count: int = 0
    last_number: int = l[0]
    list_count: List = []

    while index < len(l):
        if l[index] == last_number:
            count += 1
        else:
            list_count.append(count)
            last_number = l[index]
            count = 1

        index += 1
    list_count.append(count)

    return list_count

# print(c(lista_ejemplo))
