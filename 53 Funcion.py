valorX = 0
while valorX <= 0:
    valorX = int(input("Ingrese el valor maximo de x: "))

for x in range(0, valorX + 1, 2):
    funcion_ = x**3 + x**2 - 5
    print("Para x =", x, "f(x) =", funcion_)
