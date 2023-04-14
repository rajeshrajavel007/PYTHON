R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:"))
matrix = [] 
print("Enter the entries rowwise:")  
for i in range(R):
	a =[] 
	for j in range(C):   
		a.append(int(input())) 
	matrix.append(a) 
for i in range(R): 
	for j in range(C): 
		print(matrix[i][j], end = " ") 
	print()
	
upd = 0
lwd = 0
for i in range(R):
    for j in range(i,C):
        upd += matrix[i][j]
print("Sum of Upper Diagnol	-->",upd)
for i in range(R):
    for j in range(i):
        lwd += matrix[i][j]
print("Sum of Lower Diagnol	-->",lwd)

