import random
import string

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 17: Sistema de calificaciones con bonificaciones
## Solicita la calificación del estudiante y pregunta si hizo tareas adicionales. Si la respuesta es "sí",
## añade un 5% extra a la calificación, pero si la calificación supera 100, ajústala a 100. Si la respuesta
## es "no", simplemente muestra la calificación original.

def sistemaCalificaciones():
    calificacion = float(
        input('coloque su calificacion: ')
        )
    while True:
        tareasAdicionales = input('¿Hizo tareas adicionales? (sí/no): ').lower()
        if tareasAdicionales == 'si':
            calificacion += calificacion * 0.05
            if calificacion > 100:
                calificacion = 100
            break
        elif tareasAdicionales == 'no':
            pass
            break
        else:
            print('Respuesta invalida, coloque "sí" o "no".')
    return f'Su calificacion es {calificacion}.'

print(sistemaCalificaciones())
