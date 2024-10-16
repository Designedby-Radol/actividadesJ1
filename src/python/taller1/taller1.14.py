import random
import string

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 14: Adivinanza de letras
## Escribe un programa que permita al usuario adivinar una letra secreta usando match .

def adivinanzaLetra():
    letraSecreta = random.choice(string.ascii_lowercase)
    print(letraSecreta)
    while True:
        letraUsuario = input('Adivina una letra: ').lower()
        matc = letraUsuario == letraSecreta
        match matc:
            case True:
                return 'La letra secreta es correcta.\n'
                break
            case False:
                return 'La letra secreta es incorrecta.\n'
                continue

print(adivinanzaLetra())