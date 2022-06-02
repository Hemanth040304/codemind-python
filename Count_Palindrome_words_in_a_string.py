l = input()
l = l.split(" ")
c = 0
for i in range(len(l)):
    n = l[i].lower()
    i = 0
    j = len(n)-1
    count = 0
    if len(n)%2!=0:
        while i<=j:
            if n[i]==n[j]:
                count += 1
            i += 1
            j -= 1
        if count==len(n)//2+1:
            c+=1
    else:
        while i<j:
            if n[i]==n[j]:
                count += 1
            i += 1
            j -= 1
        if count==len(n)//2:
            c += 1
print(c)