def left_pal(x):
    temp = 0
    rev_left = 0
    while 1:
        if temp==0:
            temp = x#111
            rev_left = 0
        rev_left=rev_left*10+temp%10#11
        temp//=10#1
        if temp==0 and rev_left==x:#11==111
            break
        if temp==0 and rev_left!=x:#0
            x-=1
    return rev_left    
        
def right_pal(right):
    rev_right = 0
    temp = 0
    while 1:
        if temp==0:
            temp = right
            rev_right = 0
        rev_right=rev_right*10+temp%10
        temp//=10
        if temp==0 and rev_right==right:
            break
        if temp==0 and rev_right!=right:
            right+=1
    return rev_right        
            
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