# Escribir un programa que pregunte al usuario su edad y muestre por pantalla 
# si es mayor de edad o no.

import os
os.system("clear")

edad=int(input("Por favor, introduzca su edad: "))

if edad >= 18:
    print("¡Enhorabuena! Es mayor de edad")
else:
    print("Lo sentimos, no es mayor de edad")