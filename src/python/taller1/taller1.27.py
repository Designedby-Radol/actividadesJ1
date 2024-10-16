import random
import string

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 27: Suma de números pares hasta que se introduce un impar

def sumaPares():
    suma = 0
    while True:
        numero = int(input('Introduce un número: '))
        if numero % 2 == 0:
            suma += numero
            print(f'La suma de los números pares introducidos hasta ahora es {suma}.')
            continue
        elif numero % 2 != 0:
            print('Se ha introducido un número impar.')
            break
    return f' la suma de los pares es: {suma}'

print(sumaPares())
