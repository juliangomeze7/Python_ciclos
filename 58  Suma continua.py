suma = 0
num = 1
while num != 0:
    num = int(input("Ingrese un número: "))
    if num < 0:
        continue
    if num != 0:
        suma += num
print("Suma total:", suma)