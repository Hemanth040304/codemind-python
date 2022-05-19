string = input()
l = len(string)
for i in range(0,l):
    if string[i]=='.':
        print("[.]",end="")
    else:
        print(string[i],end="")