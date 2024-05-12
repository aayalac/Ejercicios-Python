n = int(input("Ingresa un número para calcular su factorial: "))

# Inicializa la variable 'factorial' como 1
factorial = 1

# Itera desde 1 hasta n (inclusive)
for i in range(1, n + 1):
    factorial *= i    

# Imprime el resultado
print(f"El factorial de {n} es: {factorial}")