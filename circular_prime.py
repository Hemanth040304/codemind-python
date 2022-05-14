def prime(n):
    c = 0
    for i in range(2,n//2):
        if n%i==0:
            c+=1
    if c==0:
        return True
    else:
        return False
def rev(n):
    r = 0
    while n:
        r=r*10+n%10
        n//=10
    return r
n = int(input())
if prime(n) and prime(rev(n)):
    print("circular prime")
elif prime(n) or prime(rev(n)):
    print("prime but not a circular prime")
else:
    print("not prime")