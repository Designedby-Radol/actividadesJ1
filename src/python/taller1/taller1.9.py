import random
import string
print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 9: Clasificación de edades
## Solicita la edad de la persona e indica si es niño (0-12 años), adolescente (13-17 años), adulto (18-64 años) o anciano (65 años o más).

def clasificacionEdad(edad):
    if edad <= 12:
        return 'Niño.\n'
    elif edad >= 13  or edad <= 17 :
        return 'Adolescente.\n'
    elif edad >= 18 or edad <= 64 :
        return 'Adulto.\n'
    elif edad >= 65:
        return 'Anciano.\n'
    
print(clasificacionEdad(
    int(
        input('coloque su edad para saber su categoria: ')
        )
    )
)