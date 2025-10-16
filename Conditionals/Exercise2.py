#Escribir un programa que almacene la cadena de caracteres contraseña en una
#variable, pregunte al usuario por la contraseña e imprima por pantalla si la
#contraseña introducida por el usuario coincide con la guardada en la variable sin
#tener en cuenta mayúsculas y minúsculas

import os 
os.system("clear")

password="contraseña"

usupassword=input("Por favor, introduzca la contraseña: ")

if password.lower() == usupassword.lower():
    print("La contraseña coincide")
else:
    print("Error, la contraseña no coincide")
