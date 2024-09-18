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

def  calcular_pago_energia(mes, valor_kw, total_kw_consumido, estrato):
    if mes == "enero" or mes == "febrero":
        return total_kw_consumido * valor_kw * 0.5
    elif mes == "marzo" or mes == "abril":
        return total_kw_consumido * valor_kw * 0.55
    elif mes == "mayo" or mes == "junio":
        return total_kw_consumido * valor_kw * 0.6
    elif mes == "julio" or mes == "agosto":
        return total_kw_consumido * valor_kw * 0.65
    elif mes == "septiembre" or mes == "octubre":
        return total_kw_consumido * valor_kw * 0.7
    elif mes == "noviembre" or mes == "diciembre":
        return total_kw_consumido * valor_kw * 0.75
    else:
        return "Mes no válido"

