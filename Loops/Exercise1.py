#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 
#10 veces.

import os
os.system("clear")

palabra=input("Por favor, introduzca una palabra: ")

for x in range(0,10):
    print(palabra)