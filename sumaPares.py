numeroInicio = int(input("Ingrese número de inicio: "))
numeroIndicado = numeroInicio
numeroFin = int(input("Ingrese número de fin: "))
resultado = 0

for numero in range(numeroInicio, numeroFin + 1):
    if numero % 2 == 0:        
        resultado += numero
        print(f"Suma parcial: {resultado}")

print(f"El resultado de la suma de pares entre {numeroIndicado} y {numeroFin} es: {resultado}")