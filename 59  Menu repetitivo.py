opcion = ""
while opcion != "3":
    print("1. Sumar 2. Restar 3. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print("Resultado:", a + b)
    elif opcion == "2":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print("Resultado:", a - b)
    elif opcion == "3":
        print ("Programa terminado")
    else:
        print ("Opcion invalida")
