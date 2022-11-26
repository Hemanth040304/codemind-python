a,b,c,d = map(int,input().split())
xor = (((a>>b)^(a>>c))&((1<<d)-1))
print(a^((xor<<b)|(xor<<c)))