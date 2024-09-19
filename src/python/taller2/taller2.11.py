"""
Construya un algoritmo en Python, que
permita ingresar la información de un
empleado e imprima el nombre, los apellidos
y la antigüedad. Los datos que se deben
solicitar son los siguientes:
*Nombre* Teléfono
*Año de ingreso a la empresa*Apellidos
*Edad.
"""
def datosEmpleado():
    nombre = input("Ingrese el nombre del empleado: ")
    telefono = input("Ingrese el número de teléfono del empleado: ")
    añoIngreso = int(input("Ingrese el año de ingreso a la empresa: "))
    apellidos = input("Ingrese los apellidos del empleado: ")
    edad = 2022 - añoIngreso
    print(f"Nombre: {nombre}")
    print(f"Apellidos: {apellidos}")
    print(f"Teléfono: {telefono}")
    print(f"Antigüedad: {edad} años de antigüedad")

if __name__ == "__main__":
    datosEmpleado()