a = int(input())
s = ''
n = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
while a>0:
    r=a%26
    if r==0:
        s+='Z'
        a=(a//26)-1
    else:
        s+=n[r-1]
        a//=26
print(s[::-1])