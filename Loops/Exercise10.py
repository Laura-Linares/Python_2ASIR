#Escribir un programa que pida al usuario un número entero y muestre por pantalla si
#es un número primo o no.

import os
os.system("clear")

print("Programa de comprobación de números enteros \n")
num=int(input("Por favor, introduzca un número entero: "))

divisores=0

for n in range(1,num+1):
    if num%n == 0:
        divisores+=1

if divisores == 2:
    print(f"El número {num} es primo")
else:
    print(f"El número {num} no es primo")