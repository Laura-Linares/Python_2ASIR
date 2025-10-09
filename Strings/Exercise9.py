#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato
#dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa
#anterior para que también funcione cuando el día o el mes se introduzcan con un
#solo carácter.

import os
os.system("clear")

fechanacimiento=input("Por favor, introduzca su fecha de nacimiento en formato dd/mm/aaaa: ")

fechas=fechanacimiento.split("/")
print(f"Usted nació el día {fechas[0]} del mes {fechas[1]} del año {fechas[2]}")