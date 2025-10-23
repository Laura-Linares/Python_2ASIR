#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y
#muestre por pantalla el número de veces que aparece la letra en la frase

import os 
os.system("clear")

frase=input("Por favor, introduzca una frase: ").lower()
letra=input("Por favor, introduzca una letra: ").lower()

longitud=len(frase) -1
contador=0

for l in range(0,longitud):
    if frase[l] == letra:
        contador+=1

print(f"La letra {letra} aparece {contador} veces en la frase \n")
print(f"La frase era: {frase}")
