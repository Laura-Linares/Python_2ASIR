#Escribir un programa que almacene en una lista los números del 1 al 10 y los
#muestre por pantalla en orden inverso separados por comas

import os
os.system("clear")

lista=[1,2,3,4,5,6,7,8,9,10]

listainversa=sorted(lista,reverse=True)

for n in range(len(listainversa)):
    if listainversa[n] == 1:
        print(listainversa[n])
    else:
        print(listainversa[n],end=',')