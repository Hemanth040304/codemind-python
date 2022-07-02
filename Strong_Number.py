def fact(n):
    s = 1
    while n:
        s*=n
        n-=1
    return s

n = int(input())
temp = n
s = 0
while temp:
    s+=fact(temp%10)
    temp//=10
if s==n:
    print("The number",n,'is a strong number')
else:
    print("The number",n,'is not a strong number')