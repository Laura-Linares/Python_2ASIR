# Escribir un programa que almacene las asignaturas de un curso (por ejemplo
# Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
# nota que ha sacado en cada asignatura y elimine de la lista las asignaturas
# aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el
# usuario tiene que repetir.

import os
import time
def limpiar():
    os.system("clear")

limpiar()
asignaturas=[]
notas=[]

resp=""

while resp != "salir":
    limpiar()
    print("Para dejar de introducir asignaturas, escriba 'salir'\n")
    resp=input("Introduzca el nombre de la asignatura: ")
    if resp == "salir":
        continue
    asignaturas+=[resp]
    n=float(input("Introduzca la nota de la asignatura %s: " %resp))
    notas+=[n]
    time.sleep(1)

print(asignaturas)
print(notas)

asignaturascopia=asignaturas[:]

for asig,nota in zip(asignaturascopia,notas):
    if nota >= 5:
        asignaturas.remove(asig)

print("Las asignaturas que debes repetir son: \n")
for a in asignaturas:
    print(f"---> {a}")