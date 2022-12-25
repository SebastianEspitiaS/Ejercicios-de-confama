
# se importa la librería para limpiar la pantalla
import os

# se crea una lista para almacenar los productos
productos = []

def mostrar_menu():
    # se muestra el menú
    print("1. Ingresar productos")
    print("2. Ver los productos ingresados")
    print("3. Actualizar productos")
    print("4. Eliminar productos")
    print("5. Salir")

def ingresar_productos():
    try:
        # se piden los datos del producto
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        codigo = input("Ingrese el código del producto: ")

        # se verifica si el nombre o el código del producto ya existen en la lista de productos
        producto_repetido = False
        for producto in productos:
            print(producto)
            if producto["nombre"] == nombre or producto["codigo"] == codigo:
                producto_repetido = True
                print("Ya existe un producto con ese nombre o código")
                break

        if not producto_repetido:
            # se agrega el producto a la lista de productos
            productos.append({"nombre": nombre, "precio": precio, "codigo": codigo})
            print("Producto agregado exitosamente")

    except Exception as e:
        print("Error:", e)

def ver_productos():
    # se verifica si hay productos en la lista
    if len(productos) == 0:
        # si no hay productos, se muestra un mensaje
        print("No hay productos para mostrar")
    else:
        # si hay productos, se muestra una lista con todos ellos
        print("Lista de productos:")
        for producto in productos:
            print(f" - {producto['nombre']} ({producto['codigo']}): ${producto['precio']:.2f}")

def actualizar_productos():
    try:
        print("¿Por qué campo quiere buscar el producto?")
        print("1. Por código")
        print("2. Por nombre")
        opcion_busqueda = int(input("Ingrese una opción: "))

        if opcion_busqueda == 1:
            campo_busqueda = "codigo"
            valor_busqueda = input("Ingrese el código del producto a actualizar: ")
        elif opcion_busqueda == 2:
            campo_busqueda = "nombre"
            valor_busqueda = input("Ingrese el nombre del producto a actualizar: ")
        else:
            print("Opción inválida")
            return

        producto_encontrado = False
        for producto in productos:
            if producto[campo_busqueda] == valor_busqueda:
                print("¿Qué quiere actualizar del producto?")
                print("1. Nombre")
                print("2. Precio")
                print("3. Código")
                opcion_actualizacion = int(input("Ingrese una opción: "))

                if opcion_actualizacion == 1:
                    campo_actualizacion = "nombre"
                    valor_actualizacion = input("Ingrese el nuevo nombre del producto: ")
                elif opcion_actualizacion == 2:
                    campo_actualizacion = "precio"
                    valor_actualizacion = float(input("Ingrese el nuevo precio del producto: "))
                elif opcion_actualizacion == 3:
                    campo_actualizacion = "codigo"
                    valor_actualizacion = input("Ingrese el nuevo código del producto: ")
                else:
                    print("Opción inválida")
                    return
                print("Producto actualizado exitosamente")
                producto[campo_actualizacion] = valor_actualizacion
                producto_encontrado = True
                break

        if not producto_encontrado:
            print("Producto no encontrado")

    except Exception as e:
        print("Error:", e)

def eliminar_productos():
    try:
        # se pregunta al usuario por qué campo quiere buscar el producto
        print("¿Por qué campo quiere buscar el producto?")
        print("1. Por código")
        print("2. Por nombre")
        opcion_busqueda = int(input("Ingrese una opción: "))

        if opcion_busqueda == 1:
            # se pide el código del producto a eliminar
            campo_busqueda = "codigo"
            valor_busqueda = input("Ingrese el código del producto a eliminar: ")
        elif opcion_busqueda == 2:
            # se pide el nombre del producto a eliminar
            campo_busqueda = "nombre"
            valor_busqueda = input("Ingrese el nombre del producto a eliminar: ")
        else:
            # opción inválida
            print("Opción inválida")
            return

        # se busca el producto con el criterio especificado
        producto_encontrado = False
        for i, producto in enumerate(productos):
            if producto[campo_busqueda] == valor_busqueda:
                # se elimina el producto de la lista
                del productos[i]
                producto_encontrado = True
                break

        if producto_encontrado:
            print("Producto eliminado exitosamente")
        else:
            print("No se encontró el producto con el criterio especificado")
    except Exception as e:
        print("Error:", e)

def main():
    # se muestra el menú hasta que el usuario decida salir
    while True:
        mostrar_menu()
        opcion = int(input("Ingrese una opción: "))
        print('\n')

        if opcion == 1:
            # opción para ingresar productos
            ingresar_productos()
        elif opcion == 2:
            # opción para ver los productos ingresados
            ver_productos()
        elif opcion == 3:
            # opción para actualizar productos
            actualizar_productos()
        elif opcion == 4:
            # opción para eliminar productos
            eliminar_productos()
        elif opcion == 5:
            # opción para salir del programa
            break
        else:
            # opción inválida
            print("Opción inválida")

        input('\nPresione "ENTER" para continuar...')
        # se limpia la pantalla
        os.system("clear" if os.name == "posix" else "cls")

# se ejecuta el programa
if __name__ == "__main__":
    main()
