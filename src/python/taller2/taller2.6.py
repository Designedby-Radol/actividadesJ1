"""
Escribe un programa que solicite al usuario ingresar el día, el mes y el año de
una fecha. Luego, verifica si la fecha es válida o no. Considera los diferentes
casos, como los días de cada mes y si el año es bisiesto. Muestra un mensaje
indicando si la fecha es válida o no.
"""
def esBisiesto(año):
    return año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)

def esFechaValida(dia, mes, año):
    if mes < 1 or mes > 12:
        return False
    if dia < 1:
        return False
    if mes in [1, 3, 5, 7, 8, 10, 12]:  # meses con 31 días
        return dia <= 31
    if mes in [4, 6, 9, 11]:  # meses con 30 días
        return dia <= 30
    if mes == 2:  # febrero 
        return dia  <= 29 if esBisiesto(año) else dia <= 28
    return False

def fecha():
    dia = int(input('Ingrese el día: '))
    mes = int(input('Ingrese el mes: '))
    año = int(input('Ingrese el año: '))
    if esFechaValida(dia, mes, año):
        print('La fecha es válida')
    else:
        print('La fecha no es válida')



