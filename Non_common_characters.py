s1 = input().lower()
s2 = input().lower()
s1 = set(s1)
s2 = set(s2)
s1 = str(s1)
s2 = str(s2)
s1=s1.replace(" ",'')
s2=s2.replace(" ",'')
s1=s1.replace("[",'')
s2=s2.replace("[",'')
s1=s1.replace("]",'')
s2=s2.replace("]",'')
s1=s1.replace(",",'')
s2=s2.replace(",",'')
s1=s1.replace("'",'')
s2=s2.replace("'",'')
s1=s1.replace(" ",'')
s2=s2.replace(" ",'')
c=0
for i in s1:
    if i not in s2:
        c+=1
for i in s2:
    if i not in s1:
        c+=1
print(c)