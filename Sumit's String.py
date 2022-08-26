test_case = int(input())
while test_case:
    s = input()
    length = len(s)-1
    c = 0
    for i in range(1,len(s)):
        if abs(ord(s[i-1])-ord(s[i]))==1:
            c+=1
    if c==length:
        print("YES")
    else:
        print("NO")
    test_case-=1
