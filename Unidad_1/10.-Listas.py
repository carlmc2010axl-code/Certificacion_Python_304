#Declarando una lista
try:
    materias = ["programacion", "Filosofia", "Matematicas", "Ingles"]
    print(materias[0])
    materias.append("Lengua y comunicacion")
    print(materias)
    materias[1]="iologia"
    materias.remove("Matematicas")
    print(materias)
except IndexError:
    print("Error: ese indice no existe.")