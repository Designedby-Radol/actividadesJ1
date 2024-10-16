import random
import string

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 20: Sistema de estacionamiento con tarifas progresivas
## Escribe un programa que calcule el costo de estacionamiento basado en el número de horas, con tarifas progresivas.

def estacionamiento():
    HRS = int(input('digite las horas de estacionamiento: '))
    precio = int()
    if HRS >= 1: 
        precio +=5 
    if HRS >= 2:
        precio += 4
    if HRS >= 3:
        precio += 4
    if HRS >= 4:
        precio += 4
    if HRS > 4:
        for i in range(HRS-4):
            precio += 3
    return f'el costo del estacionamiento es: ${precio}'

print(estacionamiento())
