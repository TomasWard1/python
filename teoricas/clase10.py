from typing import List

cuadrados:List[int] = []
i:int = 1
while i <= 100:
        cuadrados.append(i*i)
        i = i + 1

i:int = 0
while i < len(cuadrados):
    if cuadrados[i] % 2 == 1:
        print(cuadrados[i])
    i = i + 1
