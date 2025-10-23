#Escribir un programa que pida al usuario un número entero y muestre por pantalla
#un triángulo rectángulo como el de más abajo, de altura el número introducido.
#*
#**
#***
#****
#*****

import os
os.system("clear")

num=int(input("Por favor, introduzca un numero entero: "))

if num < 0:
    print(f"El número {num} no es un entero positivo")
else:
    asterisco='*'
    for a in range(num):
        print(f"{asterisco * (a+1)}")