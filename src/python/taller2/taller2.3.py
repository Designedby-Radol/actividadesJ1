"""
Crea un programa que solicite al
usuario ingresar una contraseña y
verifique si cumple con los siguientes
requisitos: debe tener al menos 8
caracteres y contener al menos un
número. Si la contraseña cumple con
los requisitos, muestra el
mensaje"Contraseña válida". De lo
contrario, muestra el mensaje
"Contraseña inválida".
"""

def comprobarCantraseña():
    contraseña = input('Ingrese una contraseña: ')
    if len(contraseña) >= 8 and any(char.isdigit() for char in contraseña): #comprobar si la longitud y el valor numerico es correcto
        print('Contraseña válida')
    else:
        print('contraseña no es valida')

if __name__ == '__main__':
    comprobarCantraseña()  