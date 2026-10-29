print("Hola que desea comprar?")
print("1. Camisa $120")
print("2. Pantalon $150")
print("3. Zapatos $200")
opcion = input("Ingrese el numero de la opcion que desea: ")
cantidad = int(input("¿Cuanto articulos desea comprar?"))
precio = int(input("Ingrese el precio del articulo: "))
resultado = cantidad * precio
print("El total a pagar es de $", resultado)

numero = int(input("Ingresa un numero del 1 al 10:"))
if numero <= 0:
    print("Tu numero no se acepta")
elif numero >= 1 and numero <= 10:
    i = 1
    while i <= 10:
        resultado = numero * i
        print(numero, "x", i, "=", resultado)
        i = i + 1
else:
    print("Ese numero no existe")