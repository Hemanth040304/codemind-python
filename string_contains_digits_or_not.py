n = int(input())
while n:
    a = input()
    c=0
    for i in a:
        if i.isdigit():
            c+=1
    if c>0:
        print("Yes")
    else:
        print("No")