Arreglo = [1, 15, 27, 41, 88, 23, 5, 67, 49, 79, 39, 45, 7, 8, 27]
for i in range(len(Arreglo)):
    if Arreglo[i] % 7 == 0 or Arreglo[i] % 13 == 0:
        if Arreglo[i] % 7 == 0:
            print("El numero ", Arreglo[i], "Es un múltiplo de 7")
        else:
            print("El numero ", Arreglo[i], "Es un múltiplo de 13")
    else:
        print("El numero ", Arreglo[i], "No es un múltiplo de 7 o de 13")

Arreglo = [1, 15, 27, 41, 88, 23, 5, 67, 49, 79, 39, 45, 7, 8, 27]
Ordenado = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
j = 0
k = 0
for j in range(len(Arreglo)):
    if (Arreglo[j]) % 2 == 0:
        Ordenado[k] = Arreglo[j]
        k = k + 1
j = 0
for j in range(len(Arreglo)):
    if (Arreglo[j]) % 2 != 0:
        Ordenado[k] = Arreglo[j]
        k = k + 1
l = 0
print("Ordenado", "Arreglo inicial")
for l in range(len(Ordenado)):
    print(Ordenado[l], "         ", Arreglo[l])

Arreglo = [1, 15, 27, 41, 88, 23, 5, 67, 49, 79, 39, 45, 7, 8, 27]
aux = Arreglo[0]
for n in range(1, len(Arreglo)):
    Arreglo[n - 1] = Arreglo[n]
Arreglo[n] = aux
print("Ordenado posiciones pares e impares")
for o in range(len(Arreglo)):
    print(Arreglo[o])
