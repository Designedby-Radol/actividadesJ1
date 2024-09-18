"""
Escribe un programa que solicite al
usuario ingresar su calificación en un
examen y determine si ha aprobado o
no. Si la calificación es igual o mayor a
60, muestra el mensaje "Has aprobado".
De lo contrario, muestra el mensaje "Has
reprobado".
"""
def detercalificacion():
    calificacion = float(input('Ingrese su calificación: '))
    if calificacion >= 60:
        print('Has aprobado')
    else:
        print('has reprobado')

if __name__ == '__main__':
    detercalificacion()  