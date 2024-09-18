"""
Crea un programa que solicite al
usuario un número entero positivo y
luego imprima los números desde ese
número hasta 1 utilizando un
buclewhile.
"""
def imprimirNumeros():
    num = int(input("Ingrese un número entero positivo mayor a 1: "))
    while  num >= 1:
        print(num)
        num -= 1

if __name__ == '__main__':
    imprimirNumeros()