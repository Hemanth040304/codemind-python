n = input()
#print(n)
i = 0
j = len(n)-1
count = 0
n = n.lower()
#print(n)
if len(n)%2!=0:
    while i<=j:
        if n[i]==n[j]:
            count += 1
            #print(n[i],n[j])
        i += 1
        j -= 1
    if count==len(n)//2+1:
        print(True)
    else:
        print(False)
else:
    while i<j:
        if n[i]==n[j]:
            count += 1
            #print(n[i],n[j])
        i += 1
        j -= 1
    if count==len(n)//2:
        print(True)
    else:
        print(False)