def exitOpcion():
    global isAllow
    valid = True
    opciones = ('','N','n','S','s')
    accion = input('desea ir una pestaña atras? s(no) y enter(shi)')
    if (accion not in opciones):
        print('La opcion que ud ingreso no esta permitida.......')
        exitOpcion()
    elif (bool(accion)== False):
        valid = False
    elif  (bool(accion) == True):
        valid = True
    return valid
