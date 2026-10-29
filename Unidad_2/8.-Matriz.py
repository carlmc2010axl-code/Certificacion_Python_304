#Creando una matriz
numeros =[
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]
#Ciclo externo para los indices de las filas(i)
for i in range(0, 3):
    #Ciclo interno para los indices
    for j in range(0, 3):
        print(f"[{i}] [{j}] = {numeros[i][j]}")