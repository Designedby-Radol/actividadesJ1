import src.modulos.see as see
import os
def eliminarEquipos(equipos):
    mirar =int(see.eliminarEquipos(equipos))
    largo = int(len(equipos))
    if mirar > largo or bool(mirar) == False:
        input('no puede eliminar equipos que no existen')
        os.system('clear')
        return equipos
    else:
        os.system('clear')
        equipos.pop(mirar-1)
    os.system('clear')

