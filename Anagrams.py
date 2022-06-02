a = input()
b = input()
a,b = a.lower(),b.lower()
c_a = 0
c_b = 0
for i in a:
    if i in b:
        c_a += 1
for i in b:
    if i in a:
        c_b += 1
if c_b==len(a) and c_a==len(b):
    print(True)
else:
    print(False)