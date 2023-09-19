n = int(input("n: "))

flag = 0

while n != 0:
    digit = n % 10
    if digit % 2 == 0:
        flag = 1
    n //= 10

print(flag)

