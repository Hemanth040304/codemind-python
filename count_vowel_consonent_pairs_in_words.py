s=list(map(str,input().split()))
v='AEIOUaeiou'
c=0
for i in s:
    for j in range(len(i)//2):
        if ((i[j] in v) and i[len(i)-j-1] not in v)or ((i[j]not in v) and i[len(i)-j-1]in v):
            c+=1
print(c)