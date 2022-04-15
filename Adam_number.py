n = int(input())
pow_n = n*n
rev=0
x=0
while n:
    rev=rev*10+n%10
    n//=10
pow_rev= rev*rev
while pow_rev:
    x=x*10+pow_rev%10
    pow_rev//=10
if x==pow_n:
    print(True)
else:
    print(False)