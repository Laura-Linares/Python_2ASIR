#Escribir un programa que pida al usuario dos números y muestre por pantalla su
#división. Si el divisor es cero el programa debe mostrar un error.

import os
os.system("clear")

n1=float(input("Por favor, introduzca el dividendo número: "))
n2=float(input("Por favor, introduzca el divisor número: "))

if n2 == 0:
    print("Error, el divisor no puede ser cero")
else:
    resultado=n1/n2
    print(f"El resultado de la división es: {round(resultado,2)}")