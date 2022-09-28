r=0;
s=0;
for i in range (1,100):
    g = input("Ingresa numero: ");
    if (g % 3 == 0 or g % 5 == 0):
        r=r+1;
        s=s+g;
print(r,s);