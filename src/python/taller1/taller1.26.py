
import random
import string

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 26: Adivina el número (con while ) 

def adivinaNúmero():
    numeroSecreto = random.randint(1, 100)
    intentos = 0
    while True:
        numeroUsuario = int(input('Adivina el número secreto (entre 1 y 100): '))
        intentos += 1
        if numeroUsuario == numeroSecreto:
            print(f'Felicidades! Adivinaste el número secreto en {intentos} intentos.')
            break
        elif numeroUsuario < numeroSecreto:
            print('Te has pasado de la respuesta. Prueba con un número mayor.')
            continue
        elif numeroUsuario > numeroSecreto:
            print('Te has quedado corto. Prueba con un número menor.')
            continue
        if intentos == 10:
            print(f'Perdiste. El número secreto era {numeroSecreto}.')
            break

print(adivinaNúmero())