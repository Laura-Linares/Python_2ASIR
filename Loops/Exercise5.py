#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés 
#anual y el número de años, y muestre por pantalla el capital obtenido en la inversión 
#cada año que dura la inversión

import os
os.system("clear")

dinero_a_invertir=float(input("Por favor, introduzca la cantidad a invertir: "))
interes_anual=float(input("Por favor, introduzca el interés anual: "))
num_anyos=int(input("Por favor, introduzca el número de años que desea invertir: "))
inversion=0

for x in range(1,num_anyos+1):
    print(f"Inversión en el año número {x}")
    if x == 1:
        inversion=(dinero_a_invertir*(interes_anual/100))+dinero_a_invertir
    else:
        inversion=inversion+(inversion*(interes_anual/100))
    print(f"será de {round(inversion,2)} €")

print(f"La inversión total al final de los {num_anyos} será de {round(inversion,2)} €")