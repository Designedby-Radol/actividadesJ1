import src.ingresoEquipos as ing
import src.modulos.exitProgram as ex
import os
def menu ():
    mondongo = True
    while mondongo == True:
        print("""
                    1. Ingresar equipos de torneos
                    2. Ingresar jugadores de equipos
                    3. programar partidos(fecha)
                    4. Ver resultados de partidos
                    5. salir
            """)
        decision = input('Elija la opcion a la que desea acceder: ')
        os.system('clear')
        match decision :
            case '1' :
                ing.ingreso()
            case '2' :
                pass
            case '3' :
                pass
            case '4' :
                pass
            case '5':
                mondongo = ex.exitOpcion()
