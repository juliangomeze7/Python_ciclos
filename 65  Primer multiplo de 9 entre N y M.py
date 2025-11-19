n = int(input("Ingrese N: "))
m = int(input("Ingrese M: "))
i = n
encontrado = False
while i <= m and not encontrado:
    if i % 9 == 0:
        print("Primer múltiplo de 9:", i)
        encontrado = True
    i += 1
if not encontrado:
    print("No hay múltiplos de 9 en el rango")