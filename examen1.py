contador = []
for i in range (10):
    num = float(input("ingrese un numero: "))
    if num % 3 == 0:
        contador.append(num)

print(f" en la lista de números hubieron {len(contador)} múltiplos de 3 {(contador)}")