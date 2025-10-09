#Escribir un programa que pregunte por consola el precio de un producto en euros
#con dos decimales y muestre por pantalla el número de euros y el número de
#céntimos del precio introducido.

import os
os.system("clear")

precio=input("Por favor, introduzca el precio del producto con dos decimales: ")

separacion=precio.find(".")
euros=precio[:separacion]
ctms=precio[separacion+1:]

print(f"Los euros introducidos son: {euros}")
print(f"Los céntimos introducidos son: {ctms}")