Cadena1 = 'Hola '
Cadena2 = 'Mundo'
multilinea = """Esto es una cadena de varias lineas"""
print(Cadena1 + Cadena2)#print(f{Cadena})
#Cadena de repeticion
eco = 'ja'*3
print(eco)
#Cambiar una cadena minuscula a mayuscula
tu_nombre = 'Carlos'
print(tu_nombre.upper())
print(tu_nombre.lower())
frase ="Me gusta programacion"
print(frase.replace("programacion","matematicas"))
edad = 16
Nombre = 'Carlos'
mensaje =f"Hola, me llamo\n{Nombre}\ny tengo\n{edad}\naños"
print(mensaje)
texto = "¡Felicidades por aun continuar en el CECY!!!"
cantidad_caracteres=len(texto)
print(cantidad_caracteres)
oracion = "Aprender python es divertido"
if "java" in oracion:
    print("Encontrado")
else:
    print("No esta")
#Validar contenido en cadena
nlista = "16"
print(nlista.isalpha())
print(nlista.isdigit())