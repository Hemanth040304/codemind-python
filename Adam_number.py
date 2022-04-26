n = int(input())
sq_n = n*n
rev = 0
while n:
    rev=rev*10+n%10
    n//=10
sq_rev = rev*rev
adam = 0
while sq_rev:
    adam=adam*10+sq_rev%10
    sq_rev//=10
if adam==sq_n:
    print(True)
else:
    print(False)