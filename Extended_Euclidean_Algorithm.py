def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

a = int(input())
b = int(input())
g = gcd(a,b)
i = 1 
j = -1
while ((a*i) + (b*j))!=g:
    j-=1
print(g,i,j)