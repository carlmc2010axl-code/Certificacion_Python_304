#Realizar un programa que calcule
#La compra total de 4 ariculos, si la compra total
#Es mayor a 2000 pesos me haga un descuento
#del 10% 
#DATOS DE ENTRADA
precio1 = float(input("Introduce el precio del primer producto 1: "))
precio2 = float(input("Introduce el precio del segundo producto 2: "))
precio3 = float(input("Introduce el precio del tercer producto 3: "))
precio4 = float(input("Introduce el precio del cuarto producto 4: "))
#Proceso
total = precio1 + precio2 + precio3 + precio4
if total > 2000:
    total = total - (total * 0.10)
    #total = (3000-(3000*0.10) total = 2700
    print("El total de la compra es:", total)
else:
    print("No tienes descuento, el total de la compra es:", total)
