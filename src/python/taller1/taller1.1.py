"""
Hola, este archivo van todas los ejercicios del taller 1 de python clase j1
hey, this file contains all the exercises of python workshop 1 class j1.
"""
import random
import string


# Ejercicio 1:Verificación de números pares e impares
## Escribe un programa que verifique si un número es par o impar utilizando if .

def verificar(numero):
    if numero % 2 == 0:
        return 'El número es par. ☜(⌒▽⌒)☞\n'
    else:
        return 'El número es impar. •`_´•\n'  
    
print(verificar(
    int(
        input('coloque un numero para saber si es par o impar: ')
        )
    )
)