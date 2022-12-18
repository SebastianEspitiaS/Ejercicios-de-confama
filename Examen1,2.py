import os
def borrarPantalla():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def ingresarProductos(producto):
    print('Ingrese un nuevo producto.')
    datosP[0] = input('Ingrese el nombre del producto: ').capitalize()
    datosP[1] = int(input('Ingrese el valor del producto: '))
    datosP[2] = input('Ingrese el código del producto: ')
    producto[datosP[0]] = [datosP[1], datosP[2]]
    return producto

def imprimirProductos(producto):
    print('Los productos ingresados son:\n')
    for i, d in producto.items():
        print(f'{i:10} -> vale: {d[0]:5} código: {d[1]}')
    print('')

def actualizarProductos(producto):
    pass

def eliminarProductos(producto):
    while True:
            datosP[0] = input(('Quieres eliminar un elemento de la lista? (S/N): '))
            if not datosP[0].lower() in ['si', 's', 'no', 'n']:
                print('Digita una opción correcta...')
                continue
            elif datosP[0].lower() in ['si', 's']:
                datosP[0] = input('Digita el nombre del producto que quieres eliminar: ').capitalize()
                if producto.get(datosP[0]) == None:
                    print('El nombre que acaba de ingresar no esta en la lista de productos...')
                else:
                    del producto[datosP[0]]
                    print('El producto se ha eliminado con éxito...')
            break
    return producto

datosP = [None,None,None]
producto = {}
option = None

while option != '0':
    print('1. Ingresar un nuevo producto \n2. Mostrar los productos registrados \n3. Actualizar producto \n4. Eliminar un producto \n0. Salir')
    option = input('Digita una opción: ')

    if option == '1':
        ingresarProductos(producto)

    elif option == '2':
        imprimirProductos(producto)

    elif option == '3':
        pass

    elif option == '4':
        eliminarProductos(producto)

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
