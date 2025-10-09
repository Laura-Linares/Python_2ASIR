#Escribir un programa que pregunte el nombre del usuario en la consola y después
#de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n>
#letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el
#número de letras que tienen el nombre.

import os
os.system("clear")

nombre=input("Por favor, introduzca su nombre de usuario: ").upper()

print(f"El nombre {nombre} tiene: {len(nombre)} letras")
