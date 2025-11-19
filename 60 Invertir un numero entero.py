n = int(input("Ingrese un número: "))
invertido = 0
while n > 0:
    dig = n % 10
    invertido = invertido * 10 + dig
    n //= 10
print("Número invertido:", invertido)