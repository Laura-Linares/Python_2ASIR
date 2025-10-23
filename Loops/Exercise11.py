#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla
#una a una las letras de la palabra introducida empezando por la última

import os
os.system("clear")

palabra=input("Por favor, introduzca una palabra: ")

longitud=len(palabra)-1

for p in range(longitud,-1,-1):
    print(palabra[p])