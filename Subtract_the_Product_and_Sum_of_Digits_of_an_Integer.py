n = int(input())
sum=0
pro=1
while n:
    sum+=n%10
    pro*=n%10
    n//=10
print(pro-sum)