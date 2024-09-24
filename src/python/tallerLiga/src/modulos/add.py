import src.modulos.see as see
def addEquipos(equipos):
    nombre = input('Ingrese el nombre del equipo: ').strip()
    if not nombre:
        print("El nombre del equipo no puede estar vacío.")
        addEquipos
    
    if nombre in equipos:
        print(f"El equipo '{nombre}' ya existe.")
    else:
        equipos.append(nombre)
        print(f"Equipo '{nombre}' añadido exitosamente.")
    
    mas = input('desea apuntar otro equipo? N(no) enter(si):')
    if  (bool(mas) == False) :
        addEquipos(equipos)
    else:
        print('chao')
    return equipos

def addPlantel(equipos):
    mirar = see.plantelEquipos(equipos)
    jugadores = []
    a = 11
    i = 0
    if mirar == False:
        input('vuelva al menu principal y cree un equipo para asignar un plantel')
        return
    else:
        for i in range(a):
            i =+ 1
            jugador = input('ingrese el nombre del jugador')
            jugadores.append(jugador.lower())
        equipos.append([mirar,jugadores])