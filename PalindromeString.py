def palindromeString(str):
    length= len(str)
    count = int((length/2))
    last=length-1
    flag=0
    for i in range(0,count):
        if str[i] == str[last-i]:
            flag+=1
    if flag==count:
        print("palindrome")
    else:
         print("Not palindrome")

s = input()
palindromeString(s)
