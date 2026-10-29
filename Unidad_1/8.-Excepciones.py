#Ejemplo 1 sin manejo de excepciones
try:
    numero1 = float(input("Ingrese un numero: "))
    numero2 = float(input("Ingrese otro numero: "))
    resultado = numero1 / numero2
    print(resultado)
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
except ValueError:
    print("Error: Por favor, ingrese un número válido.")