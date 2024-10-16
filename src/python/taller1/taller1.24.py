import random
import string

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 24: Factorial de un número
## Escribe un programa que solicite al usuario un número entero positivo n y calcule el factorial de
## dicho número ( n! = 1 * 2 * 3 * ... * n ). Usa un ciclo for para realizar el cálculo.

def factorial():
    n = int(input('Ingrese un número entero positivo: '))
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
        print(f'El {i}º número es {i} y el factorial es {factorial}')
        if factorial > 1000000:
            print('El factorial es demasiado grande para calcularlo a mano.')
            break
        elif factorial == 1000000:
            print('El factorial es demasiado grande para ser calculado exactamente.')
            break
    return f'El factorial de {n} es {factorial}.'

print(factorial())