import src.modulos.clear as cle
import src.modulos.add as add
def mirarEquipos(equipos):
    if equipos:
        print("Equipos disponibles:")
        for i, equipo in enumerate(equipos):
            print(f"{i+1}: {equipo[0]}")
        print('')
    else:
        print('No hay equipos registrados. \n')
    input('presione enter para salir:')
    cle.clearScreen()

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

def elegirEquipos(equipos):
    if equipos:
        print('Equipos actuales: \n')
        i = 0
        if equipos:
            print("Equipos disponibles:")
            for i, equipo in enumerate(equipos):
                print(f"{i+1}: {equipo[0]}")
        print('')
        a = int(input('ingrese el numero del equipo que desea agregar fecha : '))
        cle.clearScreen()
        return a 
    else:
        print('No hay equipos registrados. \n')
        return False

def verResultados():
    if hasattr(add.addFecha, "fechas"):
        fechas = add.addFecha.fechas
        if fechas:
            print("Fechas de partido:")
            for fecha in fechas:
                print(f"{fecha['equipo1']} vs {fecha['equipo2']} - Fecha: {fecha['fecha']} - Resultado: {fecha['resultado']}")
            input('')
            cle.clearScreen()
        else:
            print("No hay fechas de partido agregadas")
            input("")
            cle.clearScreen()
    else:
        print("No hay fechas de partido agregadas")
        input("")
        cle.clearScreen()