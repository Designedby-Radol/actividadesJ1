import random
import string
print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 7: Número positivo, negativo o cero
## Escribe un programa que determine si un número es positivo, negativo o cero usando if .

def numeroPositivoNegativoCero(numero):
    if numero > 0:
        return 'El número es positivo.\n'
    elif numero < 0:
        return 'El número es negativo.\n'
    elif numero == 0:
        return 'El número es cero.\n'
    
print(numeroPositivoNegativoCero(
    int(
        input('coloque un numero para saber si es positivo, negativo o cero: ')
        )
    )
)
