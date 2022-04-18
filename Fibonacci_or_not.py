n = int(input())
first_number=0
second_number=1
next_number=0
if n==1 or n==1:
    print(True)
else:
    c=0
    while next_number<=n:
        next_number=first_number+second_number
        first_number=second_number
        second_number=next_number
        if second_number==n:
            c+=1
            break
    if c==0:
        print(False)
    else:
        print(True)