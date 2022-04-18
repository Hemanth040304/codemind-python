n = int(input())
sq=n*n
number=n
d=0
temp=n
while temp:
    d+=1
    temp//=10
rev=0
while d:
    rev=rev*10+sq%10
    sq//=10
    d-=1
rev2=0
while rev:
    rev2=rev2*10+rev%10
    rev//=10
if rev2==number:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")