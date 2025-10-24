#Escribir un programa que pregunte el correo electrónico del usuario en la consola y
#muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante
#de la arroba @) pero con dominio ceu.es.

import os
os.system("clear")

correo=input("Por favor, introduzca su correo electrónico: ")
email=correo.split('@')

nuevocorreo=email[0]+"@ceu.es"

print(f"Su nuevo correo será: {nuevocorreo}")