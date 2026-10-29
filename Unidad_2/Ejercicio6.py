tabla = [
    ["Nombre", "Edad", "Calificacion"],
    ["Emily", 16, 7.2],
    ["Carlos yair", 16, 6.7],
    ["Leo", 15, 6.7],
    ["America", 15, 8.9],
    ["Michael", 16, 5.3],
    ["Sdanna", 16, 7.7],
    ["Carlos", 16, 6.9],
    ["Brian", 16, 3.2],
    ["Kimberly", 15, 8.7]
]

nombre = input("Ingresa el nombre: ")

filas = len(tabla)
columnas = len(tabla[0])
for i in range(filas):
    for j in range(columnas):
        if tabla[i][j] == nombre:
            print("Alumno encontrado en la posicion:", [i], [j])