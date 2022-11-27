s = input()
c = 1
for i in range(1,len(s)):
    if ord(s[i])>=65 and ord(s[i])<=90:
        c+=1
print(c)