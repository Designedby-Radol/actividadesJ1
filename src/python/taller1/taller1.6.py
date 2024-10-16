import random
import string
print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 6: Juego de adivinanza de números
## Escribe un programa que implemente un juego de adivinanza de números.

def adivinanza():
    numeroSecreto = random.randint(1, 100)
    intentos = 0
    while True:
        if intentos > 5:
            print('Has superado el numero de intentos permitidos.\n')
            print(f'Intento {intentos}: No adivinaste el numero, intentalo de nuevo.\n')
            break
        intentos += 1
        numeroUsuario = int(input('Adivina un numero del 1 al 10: '))
        if numeroUsuario == numeroSecreto:
            print('Felicidades! Adivinaste el numero secreto.\n')
            break
        elif numeroUsuario < numeroSecreto:
            print('El numero que ingresaste es menor.\n')
            continue
        elif numeroUsuario > numeroSecreto:
            print('El numero que ingresaste es mayor.\n')
            continue

print(adivinanza())
