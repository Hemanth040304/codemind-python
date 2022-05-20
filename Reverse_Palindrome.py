def rev(n):
    r=0
    while n:
        r=r*10+n%10
        n//=10
    return r
    
n = int(input())
while n:
        n+=rev(n)
        if rev(n)==n :
            print(n)
            break