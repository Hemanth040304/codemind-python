s = input().lower()
vo = 'aeiou'
c = 0
for i in vo:
    if i not in s:
        print(i,end=" ")
        c = 1
if c==0:
    print(c)