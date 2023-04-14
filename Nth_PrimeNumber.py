limit =int(input("Enter the limit until which to print the prime numbers:"))
print("Prime numbers till the limit:", limit)
for num in range(2,limit + 1):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)
