votoA = 0
votoI = 0
continuar = "1"

while continuar == "1":
    codigo = input("Ingrese su codigo: ")
    votacion = input("A [ANDROID]; I [IOS] Realiza su votación: ")

    if votacion in ("A", "a"):
        votoA += 1
    elif votacion in ("I", "i"):
        votoI += 1

    continuar = input("¿Desea realizar un nuevo voto? 1: Si, 2: No")

if votoA > votoI:
    print("La plataforma elegida es ANDROID")
elif votoI > votoA:
    print("La plataforma elegida es IOS")
else:
    print("Empate")
