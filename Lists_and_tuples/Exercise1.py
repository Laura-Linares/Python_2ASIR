#Escribir un programa que almacene las asignaturas de un curso (por ejemplo
#Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por
#pantalla

import os
os.system("clear")

asignaturas=[]

respuesta=input("Por favor, introduzca el nombre de la asignatura: ")

while respuesta != 'salir':
    if respuesta == 'salir':
        continue

    asignaturas+=[respuesta]
    print("Para salir del programa, escriba 'salir' \n")

    respuesta=input("Por favor, introduzca el nombre de la asignatura: ")

for asig in range(0,len(asignaturas)):
    print(f"--> {asignaturas[asig]}")