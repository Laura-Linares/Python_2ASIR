#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de
#interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de
#año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que
#comience leyendo la cantidad de dinero depositada en la cuenta de ahorros,
#introducida por el usuario. Después el programa debe calcular y mostrar por pantalla
#la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada
#cantidad a dos decimales.

import os 
os.system("clear")

ahorros=float(input("Introduzca la cantidad de dinero depositada en su cuenta de ahorros: "))
p_anyo=(ahorros*0.04)+ahorros
s_anyo=(p_anyo*0.04)+p_anyo
t_anyo=(s_anyo*0.04)+s_anyo

print("Según sus ahorros...")
print(f"Los ahorros que tendrá el primer año serán de {round(p_anyo,2)} €")
print(f"Los ahorros que tendrá el segundo año serán de {round(s_anyo,2)} €")
print(f"Los ahorros que tendrá el tercer año serán de {round(t_anyo,2)} €")