s = input()
l = len(s)
c = 0
for i in range(l):
    if s[i]=='I':
        print(c,end=" ")
        c+=1
    if s[i]=='D':
        print(l,end=" ")
        l-=1
print(c)