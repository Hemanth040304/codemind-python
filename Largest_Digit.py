n = int(input())
max = 0
while n:
    if max<n%10:
        max=n%10
    n//=10
print(max)