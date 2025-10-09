#Escribir un programa que pregunte el correo electrónico del usuario en la consola y
#muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante
#de la arroba @) pero con dominio ceu.es.

import os
os.system("clear")

correo=input("Por favor, introduzca su correo electrónico: ")
#encontrar la posición donde está el @ para poder cortarlo
posicion=correo.find("@")
nombre=correo[:posicion]
#una vez cortado, se añade la nueva extensión
nuevocorreo=nombre + "@ceu.es"

print(f"Su nuevo correo será: {nuevocorreo}")