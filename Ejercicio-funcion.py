print = 8;

m1 = int(input("Ingrese valor de ventas para el mes # 1:\n "))
m2 = int(input("Ingrese valor de ventas para el mes # 2:\n "))
m3 = int(input("Ingrese valor de ventas para el mes 2 3:\n "))

Ventas = [m1, m2, m3]

def promedio(Ventas):
    suma = 0
    for i in Ventas:
        suma = suma + i
    return suma / len(Ventas)

print("El promedio de ventas es: ", promedio(Ventas))
