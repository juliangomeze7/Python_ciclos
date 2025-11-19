pares = 0
impares = 0
n = 1
while n != 0:
    n = int(input("Ingrese un número: "))
    if n != 0:
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1
print("Pares:", pares)
print("Impares:", impares)