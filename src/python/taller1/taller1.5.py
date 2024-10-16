import random
import string
print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 5: Días de la semana
## Escribe un programa que, dado un número del 1 al 7, imprima el día correspondiente de la semana usando match .

def diaSemana(dia):
    match dia:
        case 1: return 'lunes\n'
        case 2: return 'martes\n'
        case 3: return 'miercoles\n'
        case 4: return 'jueves\n'
        case 5: return 'viernes\n'
        case 6: return 'sabado\n'
        case 7: return 'domingo\n'
        case _: return 'numero invalido, coloque un numero del 1 al 7\n'

print(diaSemana(
    int(
        input('coloque un numero del 1 al 7 para saber el dia de la semana: ')
        )
    )
)