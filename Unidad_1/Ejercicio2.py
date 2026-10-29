#Declarando una lista
try:
    alumnos = ["Emily", "Carlos", "America","Casillas", "Kimberly"]
    calificaciones = [7.4, 9.1, 8.2, 7.0, 10.0]
    print(alumnos[2])
    alumnos.append("Brian")
    print(alumnos)
    calificaciones[1] = 8.5
    print(calificaciones)
except IndexError:
    print("Error: ese indice no existe.")