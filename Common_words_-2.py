s1 = input().lower()
s2 = input().lower()
s1,s2 = s1.split(" "),s2.split(" ")
c = 0
for i in s1:
    if i in s2 and s2.count(i)==1 and s1.count(i)==1:
        c+=1
print(c)