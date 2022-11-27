for _ in range(int(input())):
    a = input()
    b = input()
    c = 0
    for i in range(len(a)):
        if ord(a[i])<=ord(b[i]):
            c+=1
    if c==len(a):
        print("YES")
    else:
        print("NO")