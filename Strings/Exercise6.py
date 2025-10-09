#Escribir un programa que pida al usuario que introduzca una frase en la consola y
#una vocal, y después muestre por pantalla la misma frase pero con la vocal
#introducida en mayúscula.

import os
os.system("clear")

frase=input("Por favor, introduzca una frase: ")
vocal=input("Por favor, introduzca la vocal que desea transformar: ")

nuevafrase=frase.replace(vocal,vocal.upper())

print(nuevafrase)