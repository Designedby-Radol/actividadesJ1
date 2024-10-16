
import random
import string

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 15: Cálculo del salario neto
## Solicita al usuario su salario bruto y su país de residencia. 
## Calcula el salario neto aplicando impuestos: el 20% para residentes de "País A", el 15% para "País B" y el 10% para "País C". Si el país no está en la lista, aplica un 25% de impuestos.


def calculoSalarioNeto():
    salarioBruto = float(
        input('coloque su salario bruto: ')
        )
    print('Coloque su pais de residencia', 'a: País A', 'b: País B', 'c: País C', sep = '\n')  # ejemplo: 'a' para País A, 'b' para País B, 'c' para País C, cualquier otro valor para País C
    paisResidencia = str(input().lower)
    match paisResidencia:
        case 'a':
            return salarioBruto * (1 - 0.20)
        case 'b':
            return salarioBruto * (1 - 0.15)
        case 'c':
            return salarioBruto * (1 - 0.10)
        case _:
            return salarioBruto * (1 - 0.25)

print(calculoSalarioNeto())