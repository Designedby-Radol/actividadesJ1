import random
import string
print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 11: Conversión de temperaturas
# #Escribe un programa que convierta grados Celsius a Fahrenheit o Fahrenheit a Celsius usando match .

def conversionTemperatura(temperatura, unidad):
    match unidad:
        case 1:
            return f'{temperatura * 9/5 + 32} grados Fahrenheit.'
        case 2:
            return f'{(temperatura - 32) * 5/9} grados Celsius.'
        case _:
            return 'unidad invalida, coloque C para Celsius o F para Fahrenheit.'

print(conversionTemperatura(
    float(
        input('coloque la temperatura: ')
        ),
        int(
        input('coloque la unidad (1 para Celsius, 2 para Fahrenheit): ')
        )
    )
)