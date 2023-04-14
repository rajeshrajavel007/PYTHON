R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
matrix1= []
matrix2= []
rmatrix=[]
for i in range(R): 
    a =[]
    for j in range(C): 
        a.append(0)
    rmatrix.append(a)
print("Enter the entries rowwise for matrix 1:")
for i in range(R): 
    a =[]
    for j in range(C): 
        a.append(int(input()))
    matrix1.append(a)
print("MATRIX 1 :")
for r in matrix1:
    print(r)
print("Enter the entries rowwise for matrix 2:")
for i in range(R): 
    a =[]
    for j in range(C): 
        a.append(int(input()))
    matrix2.append(a)
print("MATRIX 2 :")
for r in matrix2:
    print(r)
for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            rmatrix[i][j] += matrix1[i][k] * matrix2[k][j]
print("MULTIPLIED MATRIX :")
for r in rmatrix:
    print(r)
