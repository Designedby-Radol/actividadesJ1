"""
Escribe un programa que solicite al usuario
ingresar un número y luego muestre la tabla
de multiplicar de ese número del 1 al 10
"""
def tablaMultiplicar():
    numero = int(input("Ingrese un número: "))
    for i in range(1, 11): 
        print(f"{numero} x {i} = {numero * i}")

if __name__  == "__main__":
    tablaMultiplicar()