n = int(input())
temp = n
rev=0
while temp:
    rev= rev*10+temp%10
    temp//=10
if rev==n:
    print(True)
else:
    print(False)