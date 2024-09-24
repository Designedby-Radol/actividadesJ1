import os
def mirarEquipos(equipos):
    if equipos:
        print('Equipos actuales: \n')
        for equipo in equipos:
            print(equipo)
        print('')
    else:
        print('No hay equipos registrados. \n')
    input('presione enter para salir:')
    os.system('clear')

def eliminarEquipos(equipos):
    if equipos:
        print('Equipos actuales: \n')
        i = 0
        for equipo in equipos:
            i += 1
            print(f'{i}:_{equipo}')
        print('')
        a = int(input('ingrese el numero del equipo que desea eliminar: '))
        return  a 
    else:
        print('No hay equipos registrados. \n')
        return False

def plantelEquipos(equipos):
    if equipos:
        print('Equipos actuales: \n')
        i = 0
        for equipo in equipos:
            i += 1
            print(f'{i}:_{equipo}')
        print('')
        a = int(input('ingrese el numero del equipo que desea agregar plantel: '))
        a = a-1
        return a 
    else:
        print('No hay equipos registrados. \n')
        return False
