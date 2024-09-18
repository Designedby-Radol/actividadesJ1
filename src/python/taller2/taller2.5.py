"""
Crea un programa que pida al usuario ingresar el nombre de un país y luego
determine en qué continente se encuentra.Utiliza estructuras condicionales para
asociar cada país con su respectivo continente y muestra un mensaje con el
continente correspondiente.
"""

# pasises = {
#     'argentina' : 'america del sur',
#     'españa' : 'europa',
#     'australia ' : 'oceania',
#     'kongo' : 'africa',
#     'canada' : 'america del norte',
#     'china' : 'asia'
# }

def paisVerificar():
    print('Ingrese el nombre de uno de estos países','1.argentina','2.españa','3.australia','4.kongo','5.canada','6.china',sep='\n')
    pais = int(input('su opcion: '))
    match pais:
        case 1:
            print('pertenece a america del sur')
        case 2:
            print('pertenece a europa')
        case 3:
            print('pertenece a oceania')
        case 4:
            print('petenece a africa')
        case 5:
            print('pertenece a america del norte')
        case 6:
            print('pertenece a asia')
        case _:
            print('no se encuentra en la lista')
            

if __name__ == '__main__':
    paisVerificar()  