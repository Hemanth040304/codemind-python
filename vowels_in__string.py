s = input()
count = 0
c = "aeoiuAEIOU"
a = []
for i in s:
    if i in c:
        if i not in a:
            a.append(i)
        count+=1
if count==0:
    print("-1")
else:
    print(*a)