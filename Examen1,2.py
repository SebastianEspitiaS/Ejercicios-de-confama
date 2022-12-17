import os
def borrarPantalla():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

productos = []
datosP = [None,None,None]
producto = {}

while True:

    print('1. recibir nombre de un producto \n2. mostrar los productos registrados \n3. agregar un nuevo producto \n4. eliminar un producto \n0. Salir')

    opcion = int(input("Digita una opción: "))

    match (opcion):
        case (1):
            print("ingrese un nuevo producto:")
            datosP[0] = input('ingrese el nombre del producto: ')
            datosP[1] = int(input('ingrese el valor del producto: '))
            datosP[2] = input('ingrese el código del producto: ')

            producto[datosP[0]] = [datosP[1], datosP[2]]

            """producto["codigo"] = input('ingrese el código del producto: ')
            producto["nombre"] = input('ingrese el nombre del producto: ')
            producto["precio"] = int(input('ingrese el valor del producto: '))
            productos.append(producto)"""


            entrada = input('presione la tecla "ENTER" para volver al menu')
            borrarPantalla()

        case (2):
            print('los los productos ingresados son: ')
            for i, d in producto.items():
                print(f'{i} vale : {d[0]} codigo : {d[1]}')
            entrada = input('presione la tecla "ENTER" para volver al menu')
            borrarPantalla()


    ''''case(3):
            datosP[0] = input('Digita el nombre del producto que quieres actualizar: ')
            if productos.get(datosP[0]) != None:
                try:
                    datosP[1] = int(input('ingrese un nuevo valor para el producto: '))
                except:
                    print('el dato ingresado no es valido: ')
                else:

                    datosP[2] = input(('quiere cambiar el código del producto? si/no (s/n)'))
                    if datosP[2].lower() == 'si' or 's':
                        datosP[2] =
            case (_):
            pass'''
