

def buscar_raiz_cuadrada(n):

    a = n / 2
    resta = n - a

    while resta > 0.0001:

        raiz = ((n / a) + a) / 2

        resta = a - raiz

        a = raiz
        
    return a

print(buscar_raiz_cuadrada(9))


