import src.modulos.see as see
import src.modulos.add as add
import src.modulos.exitProgram as ex
import os

def registroPlantel(equipos):
    papas = True
    while papas : 
        print("""
                    1. Ingresar plantel tecnico
                    2. --
                    3. --
                    4. Salir
            """)
        decision = input('Elija la opcion a la que desea acceder: ')
        os.system('clear')
        match decision :
            case '1' :
                agregar = add.addPlantel(equipos)
            case '2' :
                pass
            case '3' :
                pass
            case '4' :
                papas = ex.exitOpcion()
                os.system('clear')