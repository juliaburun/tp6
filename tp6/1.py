#Escribir una función que reciba como parámetros dos números enteros. Calcular y devolver el resultado de la multiplicación de ambos valores utilizando solamen- te sumas. Por ejemplo 4 * 3 = 4 + 4 + 4 .
# coding=utf-8

def multiplicar(a, b):
    suma = 0
    while a > 0:
        
        suma += b

        a -= 1
    
    return suma

resultado = multiplicar(3,2)

print(resultado)