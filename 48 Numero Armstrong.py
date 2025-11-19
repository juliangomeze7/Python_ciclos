num = int(input("Ingrese el numero a evaluar: "))

num2 = num
contadorCifras = 0

while num2 > 0:
    cifra = num2 % 10
    num2 //= 10
    contadorCifras += 1

num2 = num
sumaCifra = 0

while num2 > 0:
    cifra = num2 % 10
    num2 //= 10
    sumaCifra += cifra ** contadorCifras

if num == sumaCifra:
    print("El numero", num, "es un numero Armstrong")
else:
    print("El numero", num, "no es un numero Armstrong")
