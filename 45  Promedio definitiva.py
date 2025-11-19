cantidadEstudiantes = int(input("Ingrese la cantidad de estudiantes: "))
contadorEstudiantes = 0
aprobaron = 0
reprobaron = 0
sumasDefinitiva = 0

while contadorEstudiantes < cantidadEstudiantes:
    codigoEstudiante = input("Ingrese el codigo del estudiante: ")
    notaDefinitiva = float(input("Ingrese la nota definitiva: "))
    
    if notaDefinitiva >= 3.0:
        aprobaron += 1
    else:
        reprobaron += 1
    
    sumasDefinitiva += notaDefinitiva
    contadorEstudiantes += 1

promedioGrupo = sumasDefinitiva / cantidadEstudiantes

print("La cantidad de estudiantes que aprobaron son:", aprobaron)
print("La cantidad de estudiantes que reprobaron son:", reprobaron)
print("El promedio del grupo es:", promedioGrupo)
