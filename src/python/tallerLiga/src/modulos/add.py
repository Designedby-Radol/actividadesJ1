import src.modulos.see as see
import src.modulos.exitProgram as ex
import src.modulos.clear as cle
import src.modulos.fechaVal as fech
def addEquipos(equipos):
    nombre = input('Ingrese el nombre del equipo: ').strip()
    if not nombre:
        print("El nombre del equipo no puede estar vacío.")
        addEquipos
    if nombre in equipos:
        print(f"El equipo '{nombre}' ya existe.")
    else:
        equipos.append([nombre, [],[]])
        print(f"Equipo '{nombre}' añadido exitosamente.")
    mas = input('desea apuntar otro equipo? N(no) ingrese(si):')
    if  (bool(mas) == False) :
        addEquipos(equipos)
    else:
        print('chao')
    return equipos

def addCoach(nombrEquipo, jugador,equipos):
    for team in equipos:
        if team[0] == nombrEquipo:
            team[2].append(jugador)  # Add jugador info to the team's jugadors list
            break
    return equipos

def addJugador(nombrEquipo, jugador,equipos):
    for team in equipos:
        if team[0] == nombrEquipo:
            team[1].append(jugador)  # Add jugador info to the team's jugadors list
            break
    return equipos

def addPlantel(equipos):
    pan = True
    while pan:
        nombrEquipo = input("ingrese el nombre del equipo: ")
        nombreJugador= input("ingrese el nombre del jugador: ")
        jugadorNumero = input("ingrese numero del jugador: ")
        jugadorPosicion = input("ingrese la posicion del jugador: ")
        print('')
        jugador = [nombreJugador, jugadorPosicion, jugadorNumero]
        equipos = addJugador(nombrEquipo, jugador,equipos)
        print(equipos)
        print('')
        pan = ex.hacerMas()
    return equipos


def addTecnico(equipos):
    pan = True
    while pan:
        nombrEquipo = input("ingrese el nombre del equipo: ")
        nombreJugador= input("ingrese el nombre del jugador: ")
        jugador = [nombreJugador]
        equipos = addCoach(nombrEquipo, jugador,equipos)
        print(equipos)
        pan = ex.hacerMas()
    return equipos

def addFecha(equipos,fechas):
    pan = True
    while pan:
        print("""
            ELIJA EL EQUIPO 1
        """)
        equipo1 = see.elegirEquipos(equipos)
        equipo1 -= 1
        cle.clearScreen()
        print("""
            ELIJA EL EQUIPO 2
        """)
        equipo2 = see.elegirEquipos(equipos)
        equipo2 -= 1
        cle.clearScreen()
        if equipo1 < 0 or equipo1 >= len(equipos) or equipo2 < 0 or equipo2 >= len(equipos):
            input("Error: Equipo no encontrado")
            cle.clearScreen()
            return
        dia = int(input('Ingrese el día: '))
        mes = int(input('Ingrese el mes: '))
        año = int(input('Ingrese el año: '))
        fecha = (dia, mes, año)
        fech.fecha(dia,mes, año)
        resultado = input("Ingrese el resultado del partido (Goles equipo 1 - Goles equipo 2): ")
        print(f"Partido agregado: {equipos[equipo1][0]} vs {equipos[equipo2][0]} - Fecha: {fecha} - Resultado: {resultado}")        
        if hasattr(addFecha, "fechas"):
            fechas = addFecha.fechas
        else:
            addFecha.fechas = []
        
        fechas.append({
        "equipo1": equipos[equipo1][0],
        "equipo2": equipos[equipo2][0],
        "fecha": fecha,
        "resultado": resultado
        })
        pan = ex.hacerMas()
        addFecha.fechas = fechas









