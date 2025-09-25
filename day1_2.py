import os

os.system("clear")

print("Calcule el área y el perímetro de su rectángulo")
base=float(input("Introduzca la base: "))
altura=float(input("Introduzca la altura: "))

area=base*altura
perimetro=(base*2)+(altura*2)

print(f"El área de su rectángulo es: {round(area,2)}")
print(f"El perímetro de su rectángulo es: {round(perimetro,2)}")
