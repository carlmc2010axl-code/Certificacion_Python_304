# Creando una matriz con el abecedario
letras = [
    ["A", "B", "C", "D", "E", "F", "G"],
    ["H", "I", "J", "K", "L", "M", "N"],
    ["O", "P", "Q", "R", "S", "T", "U"],
    ["V", "W", "X", "Y", "Z", " ", " "]
]

#Ciclo externo para los indices de las filas(i)
for i in range(0, 4):
    # Ciclo interno para recorrer las columnas
    for j in range(0, 7):
        print(f"[{i}] [{j}] = {letras[i][j]}")