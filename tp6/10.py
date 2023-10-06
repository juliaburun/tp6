#Extraer un dígito de un número. La función recibe como parámetros dos números enteros, uno será del que se extraiga el dígito y el otro indica qué cifra se desea obtener. La cifra de la derecha se considera la número 0. Retornar el valor -1 si no existe el dígito solicitado. Tener en cuenta que el número puede ser positivo o negativo. 
#Ejemplo: extraerdigito(12345, 1) devuelve 4, y extraerdigito(12345, 8) devuelve -1.


def extraer_digito(num, dig):

    contador = 0
    posicion = 0

    if num < 0:
        num = num * -1

    while num > 0:
        cifra = num % 10

        if cifra == dig:
            posicion = contador
        else:
            posicion = -1

        contador += 1

        num = num // 10
    
    return posicion

print(extraer_digito(12345, 1))

