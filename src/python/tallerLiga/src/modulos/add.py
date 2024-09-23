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


def addJugadores(jugadores):
    pass