#Obtener el dígito central de un número entero pasado como parámetro, sólo si la cantidad de dígitos es impar. Si la longitud fuera par devolver -1. 
#Ejemplo: digitocentral(12345) devuelve 3, y digitocentral(123456) devuelve -1.

def dig_central(numero):

    num = numero
    digitos = 0

    while num > 0:
        digitos += 1
        num = num // 10
    
    if digitos % 2 == 0:
        return -1
    else:
        num = numero

        divisor = 10 ** ((digitos - 1) // 2)

        num //= divisor

        return num % 10

    

print(dig_central(12345))

