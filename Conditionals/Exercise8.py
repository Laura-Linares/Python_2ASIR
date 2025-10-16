#En una determinada empresa, sus empleados son evaluados al final de cada año.
#Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir
#aumentando, traduciéndose en mejores beneficios. Los puntos que pueden
#conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores
#intermedios entre las cifras mencionadas. A continuación se muestra una tabla con
#los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida
#en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.
#Nivel Puntuación
#Inaceptable 0.0
#Aceptable 0.4
#Meritorio 0.6 o más
#Escribir un programa que lea la puntuación del usuario e indique su nivel de
#rendimiento, así como la cantidad de dinero que recibirá el usuario.

import os
os.system("clear")

print("--MEDIDOR DE DINERO CONSEGUIDO POR PUNTUACIÓN")
print("--PUNTUACIONES POSIBLES:  0.0  |  0.4  |  0.6 o más--")
puntuacion=float(input("Por favor, introduzca su puntuación: "))
mensaje="La cantidad de dinero que recibirá es de: "
dinero_puntuacion=2400
cantidad_dinero_obtenida=puntuacion*dinero_puntuacion

if puntuacion == 0.0:
    print("Su nivel es inaceptable")
    print(f"{mensaje} {cantidad_dinero_obtenida} €")
elif puntuacion == 0.4:
    print("Su nivel es aceptable")
    print(f"{mensaje} {cantidad_dinero_obtenida} €")
elif puntuacion >= 0.6:
    print("Su nivel es meritorio")
    print(f"{mensaje} {cantidad_dinero_obtenida} €")
else:
    print("Error. La puntuación no es válida")