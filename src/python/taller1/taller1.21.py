import random
import string

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 21: Clasificación de triángulos por sus ángulos
## Escribe un programa que clasifique un triángulo en agudo, obtuso o rectángulo según sus ángulos internos usando if

def trianguloAngulos():
    while True:
        ang1 = int(input('Ingrese el primer ángulo del triangulo: '))
        ang2 = int(input('Ingrese el segundo ángulo del triangulo: '))
        ang3 = int(input('Ingrese el tercer ángulo del triangulo: '))
        if ang1 + ang2 > ang3 and ang1 + ang3 > ang2 and ang2 + ang3 > ang1:
            if ang1 <= 90 and ang2 <= 90 and ang3 <= 90:
                return 'El triángulo es agudo.'
                break
            elif ang1 == 90 or ang2 == 90 or ang3 == 90:
                return 'El triángulo es rectangulo.'
                break
            elif  ang1 >= 90 or ang2 >= 90 or ang3 >= 90:
                return 'El triángulo es obtuso.'
                break
        else: 
            print('no es un triangulo')

print(trianguloAngulos())