#recorrer 20 números
números= []

for i in range(20):
    números.append(input("ingrese un numero: "))

print("\nLa lista es:\n")

for i in números:
    print(i, end=" ")
print("")
