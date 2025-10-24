#Escribir un programa que pregunte al usuario los números ganadores de la lotería
#primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor
#a mayor

import os
os.system("clear")

loteria=[]

nummax=int(input("¿Cuantos juegos de números tiene su billete de lotería? "))

for n in range(nummax):
    numero=int(input("Por favor, introduce el número %d: " %(n+1)))
    loteria+=[numero]

print("Sus números de lotería ordenados son... ")
for i in sorted(loteria):
    print(i, end=" ")
print(" ")