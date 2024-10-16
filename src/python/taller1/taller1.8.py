import random
import string
print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 8: Determinación de año bisiesto
## Escribe un programa que determine si un año es bisiesto o no.

def Bisiesto(año):
    if año % 4 == 0 and (año % 100!= 0 or año % 400 == 0):
        return 'El año es bisiesto.\n'
    else:
        return 'El año no es bisiesto.\n'
    

print(Bisiesto(
    int(
        input('coloque un año para saber si es bisiesto: ')
        )
    )
)