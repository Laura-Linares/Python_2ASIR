#Escribir un programa que pida al usuario un número entero y muestre por pantalla 
# si es par o impar

import os
os.system("clear")

numero=int(input("Por favor, introduzca un número: "))

if numero%2 == 0:
    print(f"El número {numero} es par")
else:
    print(f"El núemro {numero} es impar")