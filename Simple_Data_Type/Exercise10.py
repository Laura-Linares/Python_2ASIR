#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
#Suele hacer venta por correo y la empresa de logística les cobra por peso de cada
#paquete así que deben calcular el peso de los payasos y muñecas que saldrán en
#cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un
#programa que lea el número de payasos y muñecas vendidos en el último pedido y
#calcule el peso total del paquete que será enviado.

import os
os.system("clear")

n_payasos=int(input("Por favor, introduzca el número de payasos que se han vendido en el último pedido: "))
n_munecas=int(input("Por favor, introduzca el número de muñecas que se han vendido en el último pedido: "))

peso_total=(n_payasos*112)+(n_munecas*75)
peso_kilos=peso_total/100

#Resultados
print("")
print(f"El peso total del paquete que será enviado es de: {peso_total} g")
print("")
print(f"El peso en Kg será de: {peso_kilos}")