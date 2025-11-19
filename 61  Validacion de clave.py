clave_correcta = "1234"
intentos = 0
clave = ""
while intentos < 3 and clave != clave_correcta:
    clave = input("Ingrese la clave: ")
    if clave != clave_correcta:
        intentos += 1
if clave == clave_correcta:
    print("Acceso permitido")
else:
    print("Acceso denegado")