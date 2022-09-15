notas = [3.4, 2.3, 4.6, 2.0, 3.8]
s = 0
for i in range(len(notas)):
    s = s + notas[i]
p = s / 5
if p >= 3:
    print("Aprobó con nota: ", p)
else:
    print("Reprobo con nota: ", p)