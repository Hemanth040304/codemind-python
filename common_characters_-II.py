s1 = input().lower()
s2 = input().lower()
s1,s2 = s1.replace(" ",""),s2.replace(" ","")
a = []
for i in s1:
    if i in s2 and i not in a:
        a.append(i)
print(len(a))