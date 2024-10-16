import random
import string

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 25: Números pares en un rango
## Escribe un programa que solicite al usuario dos números enteros, un valor de inicio y un valor de fin. 
## El programa debe imprimir todos los números pares en ese rango, incluyendo los límites. Usa un ciclo for para recorrer el rango.

def numerosPares():
    inicio = int(input('Ingrese el número de inicio del rango: '))
    fin = int(input('Ingrese el número de fin del rango: '))
    for num in range(inicio, fin+1):
        if num % 2 == 0:
            print(num)

print(numerosPares())