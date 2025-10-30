#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un
#palíndromo.

import os
os.system("clear")

palabra=input("Escriba la palabra que desea comprobar: ").lower()

reversopalabra=palabra[::-1]

if palabra == reversopalabra:
    print(f"La palabra {palabra} es un palíndromo")
else:
    print(f"La palabra {palabra} no es un palíndromo")