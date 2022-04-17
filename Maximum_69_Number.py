n = int(input())
rev=0
while n:
    rev=rev*10+n%10
    n//=10
max=0
c=0
while rev:
    if rev%10==6 and c==0:
        max=max*10+9
        c=1
    else:
        max=max*10+rev%10
    rev//=10
print(max)