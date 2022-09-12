cantidad = int(input("Ingrese el numero de estudiantes del grupo: "));
i=1;
suma=0;
promedio=0;

while(i <= cantidad):
    edad = int(input("Ingrese la edad de el estudiante: "));
    suma = suma + edad;
    i = i + 1;
promedio =  suma / cantidad;
print("el promedio de edad del grupo es: ", promedio);