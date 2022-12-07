opción = None
empanada = []
print("Empezamos el programa")
print("**************************\n")

print("1. Registrar empanada")
print("2. Ver empanada")
print("0. Salir")

while opción != 0:
    opción = int(input("Digita una opción: "))
    if opción == 1:
        empanada.append(input("Digite el nombre de la empanada: "))
    elif opción == 2:
        print(f"Las empanadas registradas en 3000 pesos son: {empanada} y son deliciosas")
    elif opción == 0:
        print("Termino el programa")
        break
    else:
        print("Apreciado usuario, debe seleccionar una opción valida")
