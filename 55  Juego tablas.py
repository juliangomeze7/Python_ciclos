seguir = "1"

while seguir == "1":
    print("¿Con cuál tabla desea jugar?")
    tabla = 0
    while tabla < 1 or tabla > 20:
        tabla = int(input())

    aciertos = 0
    desaciertos = 0

    for contadorFilas in range(1, 11):
        producto = tabla * contadorFilas
        respuesta = int(input(f"Escriba el resultado de {tabla} x {contadorFilas}: "))

        if respuesta == producto:
            print("Felicitaciones")
            aciertos += 1
        else:
            print("Lo siento, ese no es el resultado")
            print("La respuesta correcta es:", producto)
            desaciertos += 1

    print("Aciertos:", aciertos)
    print("Desaciertos:", desaciertos)

    if aciertos <= 5:
        print("Insuficiente")
    elif aciertos <= 7:
        print("Aceptable")
    elif aciertos <= 9:
        print("Sobresaliente")
    else:
        print("Excelente")

    print("¿Desea volver a jugar? 1 : SI ; 2 : NO")
    seguir = input()
    while seguir not in ("1", "2"):
        seguir = input("Digite 1 para SI o 2 para NO: ")

