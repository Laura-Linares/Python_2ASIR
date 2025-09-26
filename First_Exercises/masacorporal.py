# Escribir un programa que pida al usuario su peso (en kg) y estatua (en m), calcule
# el indice de masa corporal y lo almacene en una variable, y muestre por pantalla
# la frase: Tu indice corporal calculado - redondeado con dos decimales
import os
os.system("clear")

#inicio del programa
print("PROGRAMA CALCULADOR DE MASA CORPORAL")
print("-------------------------------------")
peso=float(input("Por favor, introduzca su peso en Kg: "))
altura=float(input("Por favor, introduzca su altura en metros: "))
imc=peso/(altura**2)
print(f"Tu índice de masa corporal calculado es: {round(imc,2)}")