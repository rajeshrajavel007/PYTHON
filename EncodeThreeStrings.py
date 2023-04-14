#inputs = ["john","johny","janardhan"]
inputs = [ ip for ip in input().split()]
f=[]
m=[]
l=[]
for string in inputs:
    length = len(string)
    key = length//3
    if length%3==0:
        first = string[0:key]
        mid = string[key:length-key]
        last = string[length-key:]
        f.append(first)
        m.append(mid)
        l.append(last)
    elif length%3==1:n
        first = string[0:key]
        mid = string[key:length-len(first)]
        last = string[length-len(first):]
        f.append(first)
        m.append(mid)
        l.append(last)
    elif length%3==2:
        first = string[0:key+1]
        mid = string[key+1:length-len(first)]
        last = string[length-len(first):]
        f.append(first)
        m.append(mid)
        l.append(last)
first,mid,last="","",""
for i in range(0,len(inputs)):
    first +=f[i]
    mid += m[i]     
    last += l[i]
print("First    -->",first)
print("Middle   -->",mid)
print("Last     -->",last)
      
    
    
    
