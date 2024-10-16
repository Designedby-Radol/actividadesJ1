import random
import string

print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')

# Ejercicio 16: Cálculo del tiempo de viaje
## Solicita al usuario la distancia a recorrer (en km) y la velocidad promedio del automóvil (en km/h). 
## Calcula el tiempo de viaje en horas y minutos. Si la velocidad es mayor a 120 km/h, muestra un mensaje de advertencia.

def calculoTiempoViaje():
    distancia = float(
        input('coloque la distancia a recorrer (en km): ')
        )
    velocidadPromedio = float(
        input('coloque la velocidad promedio del automovil (en km/h): ')
        )
    if velocidadPromedio > 120:
        print('ATENCION: La velocidad promedio del automovil es muy alta, puede causar accidentes.')
    tiempo = distancia / velocidadPromedio
    horas = int(tiempo)
    minutos = int((tiempo - horas) * 60)
    return f'El tiempo de viaje es {horas} horas y {minutos} minutos.'

print(calculoTiempoViaje())