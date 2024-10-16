import random
import string

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 12: Calculadora de IMC (Índice de Masa Corporal)
## Escribe un programa que calcule el IMC y determine el estado de peso.
### Solicita al usuario su peso (en kg) y su altura (en metros). Calcula el IMC y clasifícalo en bajo peso(<18.5), peso normal (18.5-24.9), sobrepeso (25-29.9), o obesidad (>=30).

def calculadorIMC(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        return 'Bajo peso.\n'
    elif 18.5 <= imc <= 24.9:
        return 'Peso normal.\n'
    elif 25 <= imc <= 29.9:
        return 'Sobrepeso.\n'
    else:
        return 'Obesidad.\n'
    

print(calculadorIMC(
    float(
        input('coloque su peso: ')
        ),
    float(
        input('coloque su altura: ')
        )
    )
)
