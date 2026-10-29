#Ciclo externo para el numero de la base de la tabla
for i in range(1, 5):
    print(f"---Tabla del {i}---")
    #ciclo interno nos multiplica la base (i) por el numero(j)
    for j in range(1, 13):
        print(f"{i} x {j} = {i*j}")
        print(f"AQUI TERMINA LA TABLA DEL {i}")