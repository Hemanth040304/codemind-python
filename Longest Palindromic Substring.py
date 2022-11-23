a = input()
m = 0
st = ''
for i in range(len(a)):
    s = ''
    for j in range(i,len(a)):
        s+=a[j]
        if s == s[::-1]:
            if len(s)>m:
                st=s
                m=len(st)
print(st)
