#Escribir un programa que pida al usuario un número entero positivo y muestre por
#pantalla la cuenta atrás desde ese número hasta cero separados por comas

import os
os.system("clear")

numero=int(input("Por favor, introduzca un número entero positivo: "))

if numero < 0:
    print("El número introducido no es positivo")
elif numero == 0:
    print("El número cero no es válido")
else:
    for x in range(numero,-1,-1):
        if x == 0:
            print(x)
        else:
            print(x, end=",")