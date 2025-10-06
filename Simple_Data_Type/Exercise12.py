#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene
#un descuento del 60%. Escribir un programa que comience leyendo el número de
#barras vendidas que no son del día. Después el programa debe mostrar el precio
#habitual de una barra de pan, el descuento que se le hace por no ser fresca y el
#coste final total.

import os
os.system("clear")

pan=3.49
pan_d=pan-(pan*0.6)

num_pan=int(input("Por favor, introduzca el número de barras de pan vendidas que no son del día: "))

total=num_pan*pan_d

print(f"El precio habitual de la barra de pan es de {pan} €")
print(f"El descuento ofrecido por no ser fresca es del 60%, por lo que su precio será de {round(pan_d,2)} €")
print(f"Y el coste final total de las barras vendidas es de {round(total,2)} €")