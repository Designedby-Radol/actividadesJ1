import random
import string

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 10: Clasificación de notas
## Escribe un programa que asigne una calificación basada en una nota numérica. Solicita una nota numérica y clasifícala como A (90-100), B (80-89), C (70-79), D (60-69), o F (<60).

def clasificacionNota(nota): 
    if 90 <= nota <= 100:
        return 'A\n'
    elif 80 <= nota <= 89:
        return 'B\n'
    elif 70 <= nota <= 79:
        return 'C\n'
    elif 60 <= nota <= 69:
        return 'D\n'
    else:
        return 'F\n'

print(clasificacionNota(
    int(
        input('coloque una nota para saber su calificacion: ')
        )
    )
)