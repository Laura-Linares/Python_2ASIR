#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
# Los ingredientes para cada tipo de pizza aparecen a continuación.
#● Ingredientes vegetarianos: Pimiento y tofu.
#● Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
# y en función de su respuesta le muestre un menú con los ingredientes disponibles
#para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el
#tomate que están en todas las pizzas. Al final se debe mostrar por pantalla si la
#pizza elegida es vegetariana o no y todos los ingredientes que lleva.

import os
os.system("clear")

eleccion_pizza=input("¿Desea que su pizza sea vegetariana? (si/no) ").lower()
mensaje_base="llevará los ingredientes: mozzarella, tomate y"

if eleccion_pizza == 'si':
    print("Los ingredientes a seleccionar UNO son:")
    print("Pimiento")
    print("Tofu")
    ingrediente=input("Introduzca el ingrediente que desea: ").lower()
    if ingrediente == 'pimiento':
        print(f"Su pizza vegetariana {mensaje_base} {ingrediente}")
    elif ingrediente == 'tofu':
        print(f"Su pizza vegetariana {mensaje_base} {ingrediente}")
    else:
        print("Ingrediente no válido")
elif eleccion_pizza == 'no':
    print("Los ingredientes a seleccionar UNO son:")
    print("Peperoni")
    print("Jamon")
    print("Salmon")
    ingrediente=input("Introduzca el ingrediente que desea: ").lower()
    if ingrediente == 'peperoni':
        print(f"Su pizza {mensaje_base} {ingrediente}")
    elif ingrediente == 'jamon':
        print(f"Su pizza {mensaje_base} {ingrediente}")
    elif ingrediente == 'salmon':
        print(f"Su pizza {mensaje_base} {ingrediente}")
    else:
        print("Ingrediente no válido")