enero = int(input("Ventas en Enero: "))
febrero = int(input("Ventas en febrero: "))
marzo = int(input("Ventas en Marzo: "))
abril = int(input("Ventas en Abril: "))
mayo = int(input("Ventas en Mayo: "))
junio = int(input("Ventas en Junio: "))

Ventas = [enero, febrero, marzo, abril, mayo, junio]
def mayor_ventas(A):
    mayor = A[0]
    for i in range(len(A)):
        if(mayor < A[i]):
            mayor = A[i]

    return mayor

print("La venta mayor fue: ", mayor_ventas(Ventas), "en el mes de: ", Ventas)
