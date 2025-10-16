#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y
#el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y
#los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un
#programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo
#que le corresponde.

import os
os.system("clear")

nombre=input("Por favor, introduzca su nombre: ").lower()
genero=input("Por favor, introduzca su género (hombre | mujer): ").lower()

if (nombre[0] < 'm' and genero == 'mujer') or (nombre[0] > 'n' and genero == 'hombre'):
    print("Perteneces al grupo A")
else:
    print("Perteneces al grupo B")