n = int(input())
temp = n
d = 0
while temp:
    d+=1
    temp//=10
number = n
sum = 0
while n:
    sum+=(n%10)**d
    n//=10
    d-=1
if sum==number:
    print(True)
else:
    print(False)