#Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46,
#22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios

import os
os.system("clear")

listaprecios=[50,75,46,22,80,65,8]
min_precio=800000000000
max_precio=0

for precio in listaprecios:
    if precio > max_precio:
        max_precio=precio
    elif precio < min_precio:
        min_precio=precio

print(f"El precio minimo de la lista es: {min_precio}")
print(f"El precio máximo de la lista es: {max_precio}")