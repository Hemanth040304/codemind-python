a=input()
b=input()
at=[]
bt=[]
for i in a:
    if i=='#':
        at.pop()
    else:
        at.append(i)
for i in b:
    if i=='#':
        bt.pop()
    else:
        bt.append(i)
if at==bt:
    print("True")
else:
    print("False")