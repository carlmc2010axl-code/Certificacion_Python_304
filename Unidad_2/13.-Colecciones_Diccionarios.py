#Creando un diccionario
persona = {
    "Nombre" : "Carlos",
    "Edad" : 16,
    "Profesion" : "Voleibolista",
    "Estudiante" : True
}
print(persona)
#Accediendo un valor en especifico
print(persona["Edad"])
#se puede usar el metodo get()
#Es util por que no marca error si el valor no existe
print(persona.get("Profesion"))
#Modificar un valor existente
persona["Edad"] = 17
print(persona["Edad"])
#Agregar un par (clave:valor)
persona["ciudad"] = "Cecyranch"
print(persona)
#Recorrer un diccionario con un bucle
