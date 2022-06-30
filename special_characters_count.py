s = input()
#print(s)
c = 0
a = '!@#$^_~./,<>;:"?-\|+=%&*(){}[]`'
for i in s:
    if i in a:
        c+=1
print(c)