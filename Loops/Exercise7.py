# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10

import os
os.system("clear")

num=1

while num <= 10:
    print(f"\n Tabla de multiplicar del {num} \n")
    for n in range(1,11):
        print(f"{num} x {n} = {num*n}")
    num+=1