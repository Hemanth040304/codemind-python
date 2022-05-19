t = int(input())
while t:
    t-=1
    s = input()
    l = len(s)
    j = l-1
    c = 0
    for i in range(0,j):
        if s[i]!=s[j]:
            print("NO")
            c+=1
            break
        j-=1
    if c!=1:
        if l%2:
            print("YES","ODD")
        else:
            print("YES","EVEN")