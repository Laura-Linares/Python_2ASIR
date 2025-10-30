#Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y
#muestre por pantalla su producto escalar

import os
os.system("clear")

vector1=(1,2,3)
vector2=(-1,0,2)

productoescalar=0

for a,b in zip(vector1,vector2):
    productoescalar+=(a*b)

print(f"El producto escalar de los dos vectores es: {productoescalar}")