def left_pal(x):
    temp = 0
    rev = 0
    while 1:
        if temp==0:
            temp = x
            rev = 0
        rev=rev*10+temp%10
        temp//=10
        if temp==0 and rev==x:
            break
        if temp==0 and rev!=x:
            x-=1
    return rev 
        
def right_pal(right):
    rev = 0
    temp = 0
    while 1:
        if temp==0:
            temp = right
            rev = 0
        rev=rev*10+temp%10
        temp//=10
        if temp==0 and rev==right:
            break
        if temp==0 and rev!=right:
            right+=1
    return rev  
            
n = int(input())
left = n-1
l=left_pal(left)
right = n+1
r=right_pal(right)
if r-n==n-l:
    print(l,r)
elif r-n>n-l:
    print(l)
else:
    print(r)