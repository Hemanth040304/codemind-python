def lcm(a,b):
    i=1
    while 1:
        if (a*i)%b==0:
            return a*i
            break
        i+=1
        
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

T = int(input())
for i in range(0,T):
    a,b = map(int,input().split())
    print(gcd(a,b),end=" ")
    print(lcm(a,b))