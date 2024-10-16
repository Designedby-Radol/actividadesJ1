import random
import string

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 22: Suma de los primeros N números enteros
## Escribe un programa que solicite al usuario un número entero positivo n y calcule la suma de los 
## primeros n números enteros. Utiliza un ciclo for para realizar la suma.

def sumaPrimerosN():
    n = int(input('Ingrese un número entero positivo: '))
    suma = 0
    for i in range(1, n+1):
        suma += i
        print(f'El {i}º número es {i} y la suma es {suma}')
    return suma

print(sumaPrimerosN())