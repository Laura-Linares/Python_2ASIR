#Escribir un programa que almacene la cadena de caracteres contraseña en una
#variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña
#correcta.

import os
os.system("clear")

password='1234'

passw=input("Por favor, introduzca su contraseña: ")
while passw != password:
    print("Contraseña errónea, inténtelo otra vez \n")
    passw=input("Por favor, introduzca su contraseña: ")

print("La contraseña es correcta! Bienvenido/a")