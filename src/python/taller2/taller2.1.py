"""
Escribe un programa que solicite al
usuario ingresar su edad y luego
determine si es mayor de edad o no
utilizando una declaraciónif. Si la edad
es mayor o igual a 18, muestra el
mensaje "Eres mayor de edad", de lo
contrario, muestra el mensaje "Eres
menor de edad".
"""

def edadCamp():
    edad = int(input('digite su edad: '))
    limEdad = int(18)
    if edad < limEdad :
        print('eres menor de edad')
    elif edad >= limEdad :
        print('eres mayor de edad')
print(edadCamp())


