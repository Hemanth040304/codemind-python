n = int(input())
first_number=0
second_number=1
next_number=0
while next_number<=n:
    next_number=first_number+second_number
    first_number=second_number
    second_number=next_number
if n-first_number<next_number-n:
    print(first_number)
elif n-first_number==next_number-n:
    print(first_number ,next_number)
else:
    print(next_number)