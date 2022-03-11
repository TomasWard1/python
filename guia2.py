#Ejercicio 1a
def f(x:int) -> int:
    x = x + 1
    return x

# x:int = 10
# print(f(x)) #imprime 11
# print(x) #imprime 10
# print(f(x*x)) #imprime 101
# print(x) #imprime 10

#Ejercicio 1b
def f ( x :int , y : int ) -> int :
    x = 2 * x + y
    return x

# x : int = 3
# y : int = 7
# y = f(y,x) #17
# x = f(y,x) #37
# print (x , y ) #37,17
# print (x , x * x ) #37, 1369 

#ejercicio 2
def f2c(f:float) -> float:
    c = (f - 32)*(5/9)
    return c 

print(f2c(195))



