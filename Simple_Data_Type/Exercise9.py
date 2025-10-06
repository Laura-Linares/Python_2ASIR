#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
#y el número de años, y muestre por pantalla el capital obtenido en la inversión.

import os
os.system("clear")

#Comienzo del programa
capital=float(input("Por favor, introduzca la cantidad que desea invertir: "))
interes=float(input("Por favor, introduzca el interés anual: "))
anyos=float(input("Por favor, ahora introduzca el número de años: "))

interes=capital*anyos*(interes/100)

print(f"El capital obtenido sería: {round(interes,2)} €.")