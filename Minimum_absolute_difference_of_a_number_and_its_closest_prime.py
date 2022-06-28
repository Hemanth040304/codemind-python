def pri_left(x):
    while x:
        c=0
        z=2
        while z<=x//2:
            if x%z==0:
                c+=1
            z+=1
        if c==0:
            return x
        x-=1

def pri_right(x):
    while x:
        c=0
        z=2
        while z<=x//2:
            if x%z==0:
                c+=1
            z+=1
        if c==0:
            return x
        x+=1


n = int(input())
left = n
right = n
l=pri_left(left)
r=pri_right(right)
if r-n<n-l:
    print(r-n)
else:
    print(n-l)