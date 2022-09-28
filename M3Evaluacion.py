M=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
a=50
for i in range(len(M)):
    for j in range(len(M)):
        M[i][j]=a
        a=a-5
print(M)