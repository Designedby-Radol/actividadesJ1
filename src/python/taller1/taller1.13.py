import random
import string

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 13: Comparación de tres números 
## Escribe un programa que determine el mayor de tres números usando if .

def comparacionNumeros(numero1, numero2, numero3):
    if numero1 > numero2 and numero1 > numero3:
        return f'{numero1} es el mayor.\n'
    elif numero2 > numero1 and numero2 > numero3:
        return f'{numero2} es el mayor.\n'
    elif numero3 > numero1 and numero3 > numero2 :
        return f'{numero3} es el mayor.\n'
    
print(comparacionNumeros(
    int(
        input('coloque el primer numero: ')
        ),
    int(
        input('coloque el segundo numero: ')
        ),
    int(
        input('coloque el tercer numero: ')
        )
    )
)
