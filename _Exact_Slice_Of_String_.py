string = input()
first = int(input())
second = int(input())
l = len(string)
for i in range(0,l):
    if i>=first and i<=second:
        print(string[i],end="")