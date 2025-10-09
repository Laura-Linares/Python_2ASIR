#Escribir un programa que pregunte el nombre el un producto, su precio y un número
#de unidades y muestre por pantalla una cadena con el nombre del producto seguido
#de su precio con 6 dígitos enteros y 2 decimales, el número de unidades con
#tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.

import os
os.system("clear")

nombre=input("Por favor, introduzca el nombre del producto: ")
precio=float(input("Por favor, introduzca el precio del producto: "))
unidades=int(input("Por favor, introduzca el número de unidades: "))

print(f"El producto {nombre} con precio {precio:08.2f} por unidad tiene {unidades:03} unidades")
coste=precio*unidades
print(f"El coste total de todas las unidades es de: {coste:010.2f}")