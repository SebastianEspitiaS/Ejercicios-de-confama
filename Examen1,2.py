import os
def borrarPantalla():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def ingresarProductos(producto, dp):
    print('Ingrese un nuevo producto.')
    dp[0] = input('Ingrese el nombre del producto: ').capitalize()
    if producto.get(dp[0]) != None:
        print('Este producto ya esta registrado...')
    else:
        dp[1] = int(input('Ingrese el valor del producto: '))
        dp[2] = input('Ingrese el código del producto: ')
        producto[dp[0]] = [dp[1], dp[2]]
        return producto

def imprimirProductos(producto):
    print('Los productos ingresados son:\n')
    for i, d in producto.items():
        print(f'{i:10} -> vale: {d[0]:5} código: {d[1]}')
    print('')

def actualizarProductos(producto, dp):
    op = None
    while op != 0:
        print('Que quieres actualizar?\n'
            '1. Nombre del producto\n'
            '2. Precio del producto\n'
            '3. Código del producto\n'
            '0. volver al menu principal')
        op = input('Digite una opción: ')

        if op != "0":
            dp[0] = input('Ingrese el nombre del producto que quieres actualizar: ').capitalize()
            if producto.get(dp[0]) == None:
                        print('Este producto no esta en la lista...')
            else:
                match(op):
                    case ('1'):
                            dp[1] = input('Ingrese el nuevo nombre: ').capitalize()
                            producto[dp[1]] = producto[dp[0]]
                            del producto[dp[0]]
                            print(f'{producto[dp[1]] = }')
                    case('2'):
                        while True:
                            try:
                                dp[1] = int(input('Ingrese un nuevo valor para el producto, presiona "ENTER" para cancelar: ')
                                            or producto[dp[0]][0])
                            except:
                                print('El dato ingresado no es valido... ')
                            else:
                                producto [dp[0]] [0] = dp[1]
                                break
                    case('3'):
                            dp[2] = input("Ingrese el nuevo código del producto: ")
                            producto [dp[0]] [1] = dp[2]

        elif op == '0':
            break

        else:
            print('Digita una opción correcta...')
        entrada = input('Presione la tecla "ENTER" para volver al menu')
        borrarPantalla()

def eliminarProductos(producto,dp):
    dp[0] = input('Digita el nombre del producto que quieres eliminar: ').capitalize()
    if producto.get(dp[0]) == None:
        print('El nombre que acaba de ingresar no esta en la lista de productos...')
    else:
        while True:
            dp[1] = input(f'Estas seguro que quieres eliminar {dp[0]} de la lista? (S/N)')
            if not dp[1].lower() in ['si', 's', 'no', 'n']:
                print('Digite una opción correcta...')
                continue
            elif dp[1].lower() in ['si', 's']:
                del producto[dp[0]]
                print('El producto se ha eliminado con éxito...')
            else:
                print('Se ha cancelado la operación con éxito...')
            break
    return producto

datosP = [None,None,None]
producto = {}
option = None

while option != '0':
    print('1. Ingresar un nuevo producto\n'
          '2. Mostrar los productos registrados\n'
          '3. Actualizar producto\n'
          '4. Eliminar un producto\n'
          '0. Salir')
    option = input('Digita una opción: ')

    if option == '1':
        ingresarProductos(producto, datosP)

    elif option == '2':
        imprimirProductos(producto)

    elif option == '3':
        actualizarProductos(producto, datosP)

    elif option == '4':
        eliminarProductos(producto, datosP)

    elif option == '0':
        continue

    else:
        print('Ingresa una opción correcta...')
    entrada = input('Presione la tecla "ENTER" para volver al menu')
    borrarPantalla()

borrarPantalla()
print('Fin del programa...\n')

"""
productos = []
producto["código"] = input('ingrese el código del producto: ')
producto["nombre"] = input('ingrese el nombre del producto: ')
producto["precio"] = int(input('ingrese el valor del producto: '))
productos.append(producto)
"""

'''datosP[0] = input('Digita el nombre del producto que quieres actualizar: ').capitalize()
        if producto.get(datosP[0]) == None:
            print('El nombre que acaba de ingresar no esta en la lista de productos...')
        else:
            try:
                datosP[1] = int(input('Ingrese un nuevo valor para el producto: '))
            except:
                print('El dato ingresado no es valido... ')
            else:
                producto [datosP[0]] [0] = datosP[1]
                while True:
                    datosP[2] = input(('Quiere cambiar el código del producto? (S/N): '))
                    if not datosP[2].lower() in ['si', 's', 'no', 'n']:
                        print('Digite una opción correcta...')
                        continue
                    elif datosP[2].lower() in ['si', 's']:
                        datosP[2] = input("Ingrese el nuevo código del producto: ")
                        producto [datosP[0]] [1] = datosP[2]
                    break'''
