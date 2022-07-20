s = input().split(" ")
for i in range(len(s)):
    a = s[i]
    if i%2==0:
        print(a[::-1],end=" ")
    else:
        print(a,end=" ")