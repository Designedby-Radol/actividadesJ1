
import random
import string

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 23: Contador de vocales en una cadena
## Escribe un programa que solicite al usuario una cadena de texto y cuente cuántas vocales (a, e, i, o, u)
## contiene. Usa un ciclo for para recorrer la cadena y realizar la cuenta.

def contarVocales():
    cadena = input('Ingrese una cadena de texto: ')
    vocales = 'aeiouAEIOU'
    contador = 0
    for letra in cadena:
        if letra in vocales:
            contador += 1
            print(f'La letra {letra} es una vocal.')
    return f'La cadena contiene {contador} vocales.'

print(contarVocales())