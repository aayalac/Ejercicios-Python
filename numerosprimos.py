import math

numero = int(input("Ingrese un número de inicio: "))
rango = int(input("Ingrese número de fin: "))

print("Lista de numeros primos:")

for num in range(numero, rango):
    if num > 1:
        es_primo = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                es_primo = False
                break
        if es_primo:
            print(num)
