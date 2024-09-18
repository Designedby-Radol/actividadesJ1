"""
Crea un programa que solicite al usuario
ingresar una serie de números positivos y
luego calcule e imprima el promedio de los
números ingresados utilizando un bucle while.
El programa debe terminar cuando el usuario
ingrese un número negativo
"""
def calcular_promedio():
    numeros = []
    contador = input('digite cuantos numeros va a tener la lista: ')
    for i in  range(int(contador)):
        num = float(input(f'ingrese el {i+1} numero: '))
        numeros.append(num)
    return  numeros

def calcular_promedio_numeros(numeros):
    suma = 0
    for num in numeros:
        suma += num
        return suma / len(numeros)

def main():
    numeros = calcular_promedio()
    promedio = calcular_promedio_numeros(numeros)
    print(f'el promedio de los numeros ingresados es: {promedio}')

if __name__  == "__main__":
    main()