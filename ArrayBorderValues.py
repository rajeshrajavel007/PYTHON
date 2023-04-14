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
if R==1 or C==1:
    for i in range(R):
            for j in range(C):
                 print(matrix[i][j], end = " ")
else:
    i = 0
    while i<=R-2:
       for j in range(len(matrix[i])):
          if i == 0:
              print(matrix[i][j])
          elif i != 0:
              j = len(matrix[i])-1
              print(matrix[i][j])
              break
       i = i+1
    temp = len(matrix[R-1])
    k = temp - temp*2
    j = -1
    while j>=k:
        print(matrix[R-1][j])
        j = j-1
    i = R-2
    while i>=1:
        j = 0
        print(matrix[i][j])
        i = i-1


   
