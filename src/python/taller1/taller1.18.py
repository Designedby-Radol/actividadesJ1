import random
import string

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 18: Sistema de evaluación de créditos universitarios
## Solicita al usuario ingresar el número de materias que ha cursado. Para cada materia, solicita el
## puntaje y determina si ha aprobado o no (>= 60). Luego, calcula el número total de créditos del
## estudiante (cada materia aprobada otorga 3 créditos).

def sistemaCreditos():
    numeroMaterias = int(
        input('coloque el numero de materias que ha cursado: ')
        )
    creditosTotales = 0
    i = 0
    for _ in range(numeroMaterias):
        i += 1
        puntaje = float(
            input(f'coloque el puntaje de la materia {i}: ')
            )
        if puntaje >= 60:
            creditosTotales += 3
            print('La materia ha sido aprobada.')
            continue
        elif creditosTotales <= 60:
            print('La materia ha sido reprobada.')
    return f'El estudiante ha cursado {numeroMaterias} materias, y ha acumulado {creditosTotales} créditos.'

print(sistemaCreditos())