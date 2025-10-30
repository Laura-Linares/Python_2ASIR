# Escribir un programa que almacene el abecedario en una lista, elimine de la lista las
# letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista
# resultante.

import os
import string # diccionario para añadir el abecedario
os.system("clear")

abecedario=list(string.ascii_lowercase)
abc=abecedario[:]

print(abecedario)

for letra in abc:
    indice=abc.index(letra)
    if indice%3 == 0:
        abecedario.remove(letra)

print(abecedario)
