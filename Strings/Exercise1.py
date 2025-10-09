#Escribir un programa que pregunte el nombre del usuario en la consola y un número
#entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces
#como el número introducido.

import os
os.system("clear")

nombre=input("Por favor, introduzca su nombre de usuario: ")
num=int(input("Por favor, introduzca un número entero: "))

print((nombre + "\n") *num)