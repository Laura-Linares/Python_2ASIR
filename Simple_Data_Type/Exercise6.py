#Escribir un programa que lea un entero positivo,n, introducido por el usuario y
#después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma
#de los primeros enteros positivos puede ser calculada de la siguiente forma:

import os
os.system("clear")

n=int(input("Por favor, introduzca un entero positivo: "))
if n < 0:
    print("El número introducido no es un entero positivo")
else:
    suma=(n*(n+1))/2
    print(f"La suma de los {n} primeros números es: {suma}")