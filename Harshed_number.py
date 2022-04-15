n = int(input())
sum=0
temp=n
while n!=0:
    sum+=n%10
    n//=10
if temp%sum==0:
    print(True)
else:
    print(False)