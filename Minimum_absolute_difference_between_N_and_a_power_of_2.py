n = int(input())
leftpower=2
rightpower=2
while leftpower*2<=n:
    leftpower*=2
while rightpower<=n:
    rightpower*=2
if n-leftpower<rightpower-n:
    print (n-leftpower)
elif n-leftpower==rightpower-n:
    print(n-leftpower,rightpower-n)
else:
    print(rightpower-n)