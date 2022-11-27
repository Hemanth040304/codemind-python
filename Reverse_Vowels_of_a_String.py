a = input()
v = 'aeiouAEIOU'
arr = []
for i in a:
    if i in v:
        arr.append(i)
i = len(arr)-1
s = ''
for j in a:
    if j in v:
        s+=arr[i]
        i-=1
    else:
        s+=j
print(s)