n = int(input("Ingrese un número: "))
es_primo = True
if n <= 1:
    es_primo = False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            es_primo = False
if es_primo:
    print("Es primo")
else:
    print("No es primo")