t = int(input())
while t:
    t-=1
    a = input()
    l=len(a)
    c = 0
    for i in range(0,l):
        if a[i]=='0' or a[i]=='1' or a[i]=='2' or a[i]=='3' or a[i]=='4' or a[i]=='5' or a[i]=='6' or a[i]=='7' or a[i]=='8' or a[i]=='9':
            c+=1
    if c==l:
        print(True)
    else:
        print(False)