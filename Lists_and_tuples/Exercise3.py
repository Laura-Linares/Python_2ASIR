#Escribir un programa que almacene las asignaturas de un curso (por ejemplo
#Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
#nota que ha sacado en cada asignatura, y después las muestre por pantalla con el
#mensaje En <asignatura> has sacado <nota> donde <asignatura> es
#cada una des las asignaturas de la lista y <nota> cada una de las correspondientes
#notas introducidas por el usuario

import os
def limpiar():
    os.system("clear")

limpiar()

asignaturas=[]
notas=[]

respuesta=input("Por favor, introduzca el nombre de la asignatura: ")

while respuesta != 'salir':
    asignaturas+=[respuesta]

    n=float(input("Por favor, introduzca la nota de la asignatura %s: " %respuesta))
    notas+=[n]

    print("Para salir del programa, escriba 'salir' \n")

    respuesta=input("Por favor, introduzca el nombre de la asignatura: ")

    if respuesta == 'salir':
        continue
    
limpiar()

for asig,nota in zip(asignaturas,notas):
    print(f"En {asig} has sacado un {nota}")