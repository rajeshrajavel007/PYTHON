def unique_values(duplic):
    for i in duplic:
        if i not in unique:
            unique.append(i)
unique = []
print("Enter the values:")
org = list(map(int,input().split()))
unique_values(org)
print("The Unique values",unique)
sortcond = int(input("Select the sorting order:\n1.Ascending \n2.Descending \nDefault --> Ascending \n"))
if sortcond == 2:
    unique.sort(reverse = True)
    print("After sorting",unique)
    decen = int(input("Enter the rank number of the element"))
    print("The element is:",unique[decen-1])

else:
    unique.sort()
    print("After sorting",unique)
    ascen = int(input("Enter the rank number of the element"))
    print("The element is:",unique[ascen-1])