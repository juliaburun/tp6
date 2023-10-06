#Calcular y devolver el Máximo Común Divisor de dos enteros no negativos, 
#basándose en las siguientes fórmulas matemáticas:
#· MCD(X,X) = X
#· MCD(X,Y) = MCD(Y, X)
#· Si X > Y => MCD(X, Y) = MCD(X-Y, Y).
#Ejemplo: MCD(40, 15) devuelve 5.


def maximo_comun_divisor(x, y):
    while y != 0:
        x, y = y, x % y
    return x

print("El Máximo Común Divisor es:", maximo_comun_divisor(40,15))

#El bucle aprovecha la propiedad del algoritmo de Euclides, que establece que el MCD de dos números no cambia si reemplazas uno de los números por su residuo en la división por el otro número. Por lo tanto, este bucle iterará hasta que y sea igual a cero, momento en el cual x contendrá el MCD buscado.

