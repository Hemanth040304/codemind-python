n = int(input())
first = 0
second = 1
next=first+second
print(first,second,next,end=" ")
while n-3:
    first=second
    second=next
    next=first+second
    print(next,end=" ")
    n-=1