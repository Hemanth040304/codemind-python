a = input()
s1 = ""
sp = "!@#$%^&*()_+-=~`{}|[]\:;'<>?,./'"
c = 0
for i in a:
    if i in sp:
        c+=1
    if i.isdigit():
        s1+=i
arr = list(s1)
e,o = [],[]
for i in arr:
    if (ord(i)-48)%2==0:
        e.append(i)
    else:
        o.append(i)
if c%2==0:
    for i in range(max(len(e),len(o))):
        if i<len(e):
            print(e[i],end="")
        if i<len(o):
            print(o[i],end="")
else:
    for i in range(max(len(e),len(o))):
        if i<len(o):
            print(o[i],end="")
        if i<len(e):
            print(e[i],end="")
    