t = int(input())
while t:
    n = int(input())
    s = input()
    c=0
    for i in range(n):
        count=0
        for j in range(n):
            if s[i]==s[j]:
                count+=1
        if count==1:
            print(s[i])
            c+=1
            break
    if c==0:
        print('-1')
    t-=1