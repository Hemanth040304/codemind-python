for _ in range(int(input())):
    n = int(input())
    s1,s2 = 0,0
    while s1<n:
        s2=s1
        s1=2*s1+1
    print(s2)