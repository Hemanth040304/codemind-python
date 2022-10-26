n = int(input())
s = bin(n)
s = s[2::]
k = ''
for i in s:
    if i=='0':
        k+='1'
    elif i=='1':
        k+='0'
print(int(k,2))