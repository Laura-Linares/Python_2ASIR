#Los teléfonos de una empresa tienen el siguiente formato
#prefijo-número-extension donde el prefijo es el código del país +34, y la
#extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un
#programa que pregunte por un número de teléfono con este formato y muestre por
#pantalla el número de teléfono sin el prefijo y la extensión.

import os
os.system("clear")

print("Teléfono en formato prefijo-número-extensión")
print("Ej. +xx-xxxxxxxxx-xx")
telefono=input("Introduzca su teléfono: ")

num=telefono[4:-3]

print(f"Su número de télefono es: {num}")