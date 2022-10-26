for _ in range(int(input())):
    n = input()
    s = bin(int(n,8))
    print(s[2::])