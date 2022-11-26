s = input().lower()
a = 'qwertyuiopalskdjfhgmznxbcv'
x = ''
for i in s:
    if i in a:
        x+=i
if x==x[::-1]:
    print("true")
else:
    print("false")