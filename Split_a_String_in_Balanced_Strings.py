n = input()
c=0
p=len(n)
i=0
count=0
while p:
    if n[i]=="R":
        c+=1
    else:
        c-=1
    i+=1
    if c==0:
        count+=1
    p-=1
print(count)