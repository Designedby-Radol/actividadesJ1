import random
import string
print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 2: Calificación de una nota
## Escribe un programa que determine si una nota numérica es "Aprobado" o "Reprobado" usando if .

def calificacion(nota):
    if nota >= 60:
        return 'Aprobado ƪ(ړײ)\n'
    elif nota < 60:
        return 'Reprobado \n'

print(calificacion(
    int(
        input('coloque la calificacion para saber si es aprobado o reprobado: ')
        )
    )
)