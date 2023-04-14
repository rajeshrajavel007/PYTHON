def test(virus,patients):
    tempvirus = list(virus)
    count = 0
    for i in range(len(patients)):
        for j in range(len(virus)):
            if patients[i] == virus[j]:
                if patients[i] in tempvirus:
                    subseq = tempvirus.index(patients[i])
                    del tempvirus[0:subseq+1]
                    count+=1
                    if count == len(patients):
                        result.append("POSITIVE")
                        break
                else:
                    result.append("NEGATIVE")
result = []
virus = input()    #Enter the virus code here
N = int(input()) #Enter the no.of patients
for i in range(0,N):
    patients = input() #Enter the patients report code 
    test(virus,patients)
for j in range(0,N):
    print(result[j])
    
