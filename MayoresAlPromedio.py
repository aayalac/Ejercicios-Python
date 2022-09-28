suma = 0
mayores = []
for i in range(0, 101):
    suma = suma + i
    promedio = suma / 100
for i in range(0, 101):
    if i > promedio:
        mayores.append(i)
print(f"El promedio es {promedio}")
print(f"Hay {len(mayores)} números mayores al promedio")
print(f"Los numeros mayores al promedio son{mayores}")
