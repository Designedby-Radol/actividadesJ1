import random
import string
print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 4: Determinación del tipo de triángulo
## Escribe un programa que determine el tipo de triángulo en función de sus lados usando if .

def triangulo(lado1, lado2, lado3):
    if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado1 + lado3 > lado2:
        if lado1 == lado2 == lado3:
            return 'El triangulo es equilatero.\n'
        elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
            return 'El triangulo es isosceles.\n'
        elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
            return 'El triangulo es escaleno.\n'
    else: 
        return 'no es un triangulo.\n'

print('elija el tamaño de los lados del triangulo para saber que tipo de triangulo es\n')
lado2 = int(input('lado 1: '))
lado1 = int(input('lado 2: '))
lado3 = int(input('lado 3: '))
print(triangulo(lado1, lado2, lado3))