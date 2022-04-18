n = int(input())
sum = 0
temp = n
while temp:
    sum+=temp%10
    temp//=10
if n%sum==0:
    print(True)
else:
    print(False)