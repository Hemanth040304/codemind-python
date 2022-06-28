n = int(input())
temp = n
su,rev=0,0
while n:
    rev=rev*10+n%10
    n//=10
i = 1
while rev:
    su+=(rev%10)**i
    rev//=10
    i += 1
if su==temp:
    print(True)
else:
    print(False)