#Dados dos parámetros enteros A y B, obtener A^B (A elevado a la B) mediante multiplicaciones sucesivas, utilizando la función del ejercicio anterior para multiplicar. Por ejemplo 4^3 = 4 * 4 * 4.
# coding=utf-8

def multiplicar(a, b):
    suma = 0
    while a > 0:
        suma += b
        a -= 1
    return suma

def elevar(a, b):
    contador = b
    resultado = 1
    while contador > 0:
        
        resultado = multiplicar(resultado, a)
        contador -= 1

    return resultado

print(elevar(2,5))

