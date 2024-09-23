import src.modulos.add as add
import src.modulos.exitProgram as ex
import src.modulos.delete as  del_
import os 
equipos = []
def ingreso():
    papas = True
    while papas :
        global equipos 
        print("""
                    1. Ingresar equipo
                    2. Eliminar equipo
                    3. Ver equipos
                    4. Salir
            """)
        decision = input('Elija la opcion a la que desea acceder: ')
        os.system('clear')
        match decision :
            case '1' :
                equipos = add.addEquipos(equipos)
                os.system('clear')
            case '2' :
                pass
            case '3' :
                if equipos:
                    print("Equipos actuales:", equipos)
                else:
                    print("No hay equipos registrados.")
            case '4' :
                papas = ex.exitOpcion()
                os.system('clear')