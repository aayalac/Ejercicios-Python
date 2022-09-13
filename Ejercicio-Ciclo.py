numero = int(input("Ingrese numero: "))
contador = 0
divisores = ""
for i in range(1, numero):
    if numero % i == 0:
        contador = contador + 1
        divisores = divisores + str(i) + " " + "'"
        print("El numero tiene", contador, "divisores")
        print("Los divisores de ", numero, "son", divisores)
