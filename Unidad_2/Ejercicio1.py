numero = int(input("Ingresa un numero del 1 al 10 :"))
if numero <= 0:
    print("Tu numero no se acepta")
elif numero >= 1 and numero <= 10:
    i = 1
    for i in range(1, 11):
        resultado = numero * i
    print (numero, "x", i, "=", resultado)
    i = i + 1
else:
    print("Ese numero no existe")