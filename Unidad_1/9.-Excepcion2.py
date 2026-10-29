try:
    numero1 = float(input("ingresa el primer numero :"))
    numero2 = float(input("ingresa el segundo numero :"))
    resultado = numero1 / numero2
    print("El resultado es:", resultado)
except ValueError:
    print("Solo introduce numeros")
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")
else:
    print("La division se realizo correctamente")
finally:
    print("Fin del programa.")