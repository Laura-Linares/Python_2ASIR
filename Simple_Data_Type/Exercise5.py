#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el
#coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

n_horas=float(input("Por favor, introduzca el número de horas trabajadas: "))
coste_hora=float(input("Por favor, introduzca el coste por hora: "))

resultado=n_horas*coste_hora

print(f"La paga que le corresponde es: {resultado} €")