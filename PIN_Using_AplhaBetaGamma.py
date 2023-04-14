num1 = int(input())
num2 = int(input())
num3 = int(input())
pin=0
final = []
maxlst = []
while(num1!=0):
    temp1 = num1%10
    temp2 = num2%10
    temp3 = num3%10
    maxlst.append(temp1)
    maxlst.append(temp2)
    maxlst.append(temp3)
    small = min(min(temp1,temp2),temp3)
    final.append(small)
    num1 = num1//10
    num2 = num2//10
    num3 = num3//10

big = max(maxlst)
final.append(big)
print(final)
for i in range(3,-1,-1):
    pin = pin*10+final[i]
print(pin)
    
               
