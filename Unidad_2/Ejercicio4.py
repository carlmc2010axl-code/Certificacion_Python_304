#El mapa del tersoro
mapa = [
    [".", ".", ".", "."],
    [".", ".", "X", "."],
    [".", ".", ".", "."],
    [".", ".", ".", "."]
]
filas = len(mapa)
columnas = len(mapa)
#Recorriendo la matriz con ciclos animados
#Ciclo externo para manejar filas (i)
for i in range(filas):
    for j in range(columnas):
        #Verificamos si encontramos el tesoro
        if mapa [i][j] == "X":
            print(f"Tesoro encontrado en la posicion [{i}][{j}]")