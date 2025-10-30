#Escribir un programa que pida al usuario una palabra y muestre por pantalla el
#número de veces que contiene cada vocal.

import os
os.system("clear")

a=0
e=0
i=0
o=0
u=0

palabra=input("Introduzca una palabra: ")

for p in palabra:
    if p == "a":
        a+=1
    elif p == "e":
        e+=1
    elif p == "i":
        i+=1
    elif p == "o":
        o+=1
    elif p == "u":
        u+=1

print(f"La palabra {palabra} tiene: \n")
print(f"a --> {a}   e --> {e}   i --> {i}   o --> {o}   u --> {u}")
