#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos
#los años que ha cumplido (desde 1 hasta su edad).

import os
os.system("clear")

edad=int(input("Por favor, introduzca su edad: "))
print("Los años que ha cumplido son:")
for x in range(1,edad+1):
    print(x)