#Escribir un programa que pida al usuario un número entero positivo y muestre 
#por pantalla todos los números impares desde 1 hasta ese número separados 
#por comas

import os
os.system("clear")

numero=int(input("Por favor, introduzca un número entero positivo: "))

if numero < 0:
    print("El número introducido no es positivo")
elif numero == 0:
    print("El número cero no es válido")
else:
    for x in range(1,numero+1):
        if x%2 != 0:
            print(x, end=",")