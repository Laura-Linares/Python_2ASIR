#Escribir un programa que pregunte el nombre del usuario en la consola y después
#de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!,
#donde <nombre> es el nombre que el usuario haya introducido.

import os
os.system("clear")

name=input("Por favor, introduzca su nombre de usuario: ")
print(f"¡Hola {name}!")