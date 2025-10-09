#Escribir un programa que pregunte por consola por los productos de una cesta de la
#compra, separados por comas, y muestre por pantalla cada uno de los productos en
#una línea distinta.

import os
os.system("clear")

cesta=input("Por favor, introduzca los productos de la cesta de la compra, separados por una \",\": ")

productos=cesta.replace(",","\n")
print("Su lista de la compra es:")
print(productos)