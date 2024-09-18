def numerosPares():
    inicio = int(input('Ingrese el número de inicio del rango: '))
    fin = int(input('Ingrese el número de fin del rango: '))
    for num in range(inicio, fin+1):
        if num % 2 == 0:
            print(num)

print(numerosPares())