#Escribir un programa que pida al usuario que introduzca una frase en la consola y
#muestre por pantalla la frase invertida.

import os
os.system("clear")

frase=input("Por favor, introduzca una frase: ")
fraseinvertida=frase[::-1]

print(fraseinvertida)