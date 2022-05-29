n , m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = set(a)
d = set(b)
arr1 =[]
arr2 = []
arr1 = c
arr2 = d
count = 0
for i in arr1:
    if i not in arr2:
        count+=1
for i in arr2:
    if i not in arr1:
        count+=1
print(count)