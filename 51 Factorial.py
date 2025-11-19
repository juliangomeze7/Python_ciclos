num = int(input("Ingrese el numero para el factorial: "))

if num < 0:
    print("No se puede calcular el factorial")
else:
    factorial_ = 1
    inferiores = 1

    while inferiores <= num:
        factorial_ *= inferiores
        inferiores += 1

    print("El factorial de", num, "es:", factorial_)
