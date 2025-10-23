#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta
#que el usuario escriba “salir” que terminará

def limpiar():
    import os
    os.system("clear")

limpiar()

print("Repito todo lo que escribes! \n")

frase=input("Escribe algo! ")

while frase != 'salir':
    print(f"Has escrito... \n {frase} \n")
    print("Para salir introduce 'salir' \n")
    frase=input("Escribe algo! ")
    limpiar()