n = int(input("Ingrese un número: "))
for i in range(n, -1, -1):
    if i % 7 == 0 and i != 0:
        print(i, "¡Alerta múltiplo de 7!")
    else:
        print(i)