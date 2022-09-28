t = int(input())
arr = []
for i in range(t):
    n = int(input())
    arr.append(n)
for i in range(t):
    if arr[i]>296:
        arr[i]%=296
    if arr[i]%10==0:
        print("sunday")
    elif arr[i]%10==1:
        print("monday")
    elif arr[i]%10==2:
        print("tuesday")
    elif arr[i]%10==3:
        print("wednesday")
    elif arr[i]%10==4:
        print("thursday")
    elif arr[i]%10==5:
        print("friday")
    elif arr[i]%10==6:
        print("saturday")
    elif arr[i]%10==7:
        print("kryptonday")
    elif arr[i]%10==8:
        print("coluday")
    elif arr[i]%10==9:
        print("daxamday")
