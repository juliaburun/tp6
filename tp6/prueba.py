def hasta_fin_de_mes(d, m, a):

    if ((m <= 7 and m % 2 != 0) or (m >= 7 and m % 2 == 0)): #mes de 31 dias
        dias = 31 - d
    elif ((m >= 7 and m % 2 != 0) or (m <= 7 and m % 2 == 0) and m != 2): #mes 30 dias
        dias = 30 - d
    elif m == 2 and ((a % 4 == 0 and a % 100 != 0) or (a % 400 == 0)): #bisiesto
        dias = 29 - d
    elif m == 2 and ((a % 4 != 0) or (a % 100 == 0)): # no bisiesto
        dias = 28 - d

    return dias

print(hasta_fin_de_mes(30, 3, 2022))