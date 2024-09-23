import src.modulos.add as add
import src.modulos.exitProgram as ex
import src.modulos.delete as  del_
import src.modulos.see as see
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
                eliminar = del_.eliminarEquipos(equipos)
            case '3' :
                mirar = see.mirarEquipos(equipos)
            case '4' :
                papas = ex.exitOpcion()
                os.system('clear')