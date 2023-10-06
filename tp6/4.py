#Devolver True si el número entero recibido como primer parámetro es múltiplo del segundo, o False en caso contrario. Ejemplo: esmultiplo(40, 8) devuelve True y esmultiplo(50, 3) devuelve False.

def es_multiplo(a, b):

    if a % b == 0:
        return True
    else:
        return False

es_multiplo(50, 3)