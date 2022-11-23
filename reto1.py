#hamburguesa el coral
print("************************")
print("Hamburguesas el Corral")
print("************************")
nombre = input("Escriba su nombre: ")
cedula = input("Esciba su numero de cedula: ")
pedido = input("Que hamburguesa va a pedir: ")
valorHamburguesa = int(input("Valor de la Hamburguesa: "))
cantidad = int(input("Cuantas hamburguesas va pedir: "))
total = cantidad * valorHamburguesa

print("----------------------------")
print(f"{nombre} tu pedido fue:\n{cantidad} hamburguesas de {pedido} \npor un valor total de: {total}")
print("----------------------------")

