#Escribir un programa que pida al usuario dos números enteros y muestre por
#pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde
#<n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente
#y el resto de la división entera respectivamente.

import os
os.system("clear")

n=int(input("Por favor, introduzca el primer número entero: "))
m=int(input("Por favor, introduzca el segundo número entero: "))

c=n/m
r=n%m

print(f"El número {n} entre {m} da un cociente de {c} y un resto de {r}")