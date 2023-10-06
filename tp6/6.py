#Escribir la función comparar(a, b) que reciba como parámetros dos números en- teros y devuelva 1 si el primero es mayor que el segundo, 0 si son iguales o -1 si el primero es menor que el segundo. En este ejercicio debe aprovecharse la función del ejercicio anterior. Ejemplo: comparar(4, 2) devuelve 1, y comparar(2, 4) devuelve -1.
def signo(a):
    if a > 0:
        return 1
    elif a < 0:
        return -1
    else:
        return 0

def comparar(a,b):

    c = a - b

    if signo(c) == 1:
        return 1
    elif signo(c) == 0:
        return 0
    else:
        return -1

print(comparar(4,4))



