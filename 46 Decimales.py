num = int(input("Ingrese un numero entero del grupo decimal: "))

if num > 0:
    num2 = num
    contador = 0
    suma = 0
    
    while num2 > 0:
        residuo = num2 % 10
        num2 = num2 // 10
        suma += residuo
        contador += 1

    print("La cantidad de cifras de", num, "es", contador)
    print("La sumatoria de sus cifras es:", suma)
else:
    print("El numero es negativo")
