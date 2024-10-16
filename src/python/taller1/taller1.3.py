import random
import string
print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 3: Calculadora básica
## Utiliza match para implementar una calculadora simple.

def calculadora(a: int, b: int, operacion: str) :
    match operacion:
        case 1 : 
            return   f'{a} + {b} = {a + b}\n'
        case 2 : 
            return   f'{a} * {b} = {a * b}\n'
        case 3 : 
            return   f'{a} - {b} = {a - b}\n'
        case 4 :
            return   f'{a} / {b} = {a / b}\n'
        case _ :                 
            return 'operacion invalida\n'
    

a = int(input('asigne un valor que nececite operar: '))
b = int(input('asigne otro valor: '))
print(' ','elija la operacion que desea realizar: ', '1_+suma', '2_*multiplicacion', '3_-resta', '4_/divicion',sep = '\n' )
operacion = int(input())
print(calculadora(a , b , operacion))
