n = int(input("n: "))

desc = True
last_digit = n % 10
while n != 0:
    digit = n % 10
    if digit < last_digit:
        desc = False
        break
    last_digit = digit
    n //= 10

if desc:
    print("Giam")
else:
    print("Khong giam")