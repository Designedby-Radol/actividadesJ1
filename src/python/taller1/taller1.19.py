import random
import string

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 19: Conversión de calificaciones numéricas a letras
## Escribe un programa que convierta una calificación numérica en una letra de acuerdo a un sistema de calificación específico, usando match .

def calificacionLetra():
    calificacion = int(input('Introduce la calificacion numerica (0-100): '))
    match calificacion:
        case n if 90 <= n <= 100:
            return 'Tu calificación en letra es: A'
        case n if 80 <= n < 90:
            return 'Tu calificación en letra es: B'
        case n if 70 <= n < 80:
            return 'Tu calificación en letra es: C'
        case n if 60 <= n < 70:
            return 'Tu calificación en letra es: D'
        case n if 0 <= n < 60:
            return 'Tu calificación en letra es: F'
        case _:
            return 'Calificación inválida'

print(calificacionLetra())