inputs = [ ip for ip in input().split()] #getting inputs in string format
unstable_list = []
stable_list = []
count = 0 #count of each digit
freq = 0 #frequency of the digits in number
stable_flag = 0
max_unstable_num = 0
min_stable_num = 99
for num in inputs: #for taking a number in the list
    length = len(num)
    for i in range(0,length): #taking first digit of the number eg:num=233 -> digit=2
        for j in range(0,length):
            if num[i] == num[j]: #used to count the occurences of a digit
                count+=1
        if i==0: #for first digit, we take the frequency of the first digit
            freq=count
            count=0
            stable_flag = 1 #variable condition used to identify the stable num
        elif freq == count: #checking the previously found frequency of a digit with current count of the digit in the number
            freq = count
            count=0
            stable_flag = 1
        else:
            unstable_list.append(int(num)) #if frequency is not same as count of the other digit, add the num in unstable list
            count=0
            freq=0
            stable_flag = 0 #set the flag to 0 as it is not a stable number
            break #break the current loop to check the next number
    freq=0
    if stable_flag == 1: #add the stable num in the stable list if flag is set to 1
        stable_list.append(int(num))
        stable_flag = 0
for stable_num in stable_list: #used to find the minimum stable number
    if min_stable_num >= stable_num:
        min_stable_num = stable_num
for unstable_num in unstable_list:  #used to find the maximum unstable number
    if max_unstable_num <= unstable_num:
        max_unstable_num = unstable_num
password = max_unstable_num - min_stable_num #difference the max unstable num to stable num to get password
print(password)


