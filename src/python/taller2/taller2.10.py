"""
En su casa le solicitan que
realice un algoritmo en Python,
que permita calcular el valor a
pagar por concepto de energía
eléctrica. Los datos que se
conocen son los siguientes:
-Mes de consumo
-Valorkw
-Totalkwconsumido en el mes
-estrato
"""

def valores():
    try:#estoy probando esto lo lei en la documentacion
        print ('Ingrese el mes de consumo: ', '1_:enero ', '2_:ebrero', '3_:marzo', '4_:abril', '5_:mayo', '6_:junio', '7:_julio', '8_:agosto', '9_:septiembre', '10_:octubre','11_:noviembre','12_:diciembre',sep ='\n' )
        mes = int(input(': '))
        totalKwConsumido = int(input('Ingrese el total kw consumido: '))
        estrato = int(input('Ingrese el estrato(1-6): '))
    except ValueError: #estoy probando esto lo lei en la documentacion
        print("Por favor, introduce un valor válido.")
    return mes, totalKwConsumido, estrato

def calcularValores(estrato ,mes):
    multiEstrato = float(0.0)
    if estrato != 1:
        multiEstrato = 0.5
        for i in range(estrato-1):
            i += 1
            multiEstrato += 0.05
    else:
        multiEstrato = 0.5
    multiEstrato = round(multiEstrato, 3)
    valorKw = 0
    print(mes)
    if mes in [6,5,11,12]:
        valorKw = 5
    elif mes in [1,2,3,4,7,8,9,10]:
        valorKw = 4
    return valorKw,multiEstrato


def calculadoraEnergetica(valorKw, totalKwConsumido, multiEstrato ):
    return round(totalKwConsumido * valorKw * multiEstrato,2)

def main():
    mes, totalKwConsumido, estrato = valores()
    valorKw,multiEstrato = calcularValores(estrato, mes)
    pago = calculadoraEnergetica(valorKw,totalKwConsumido, multiEstrato)
    print(f'El valor a pagar por concepto de energía eléctrica es: ${pago}')

if __name__ == '__main__':
    main()