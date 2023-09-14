n = int(input("n: "))

smallest_digit = n % 10
while n != 0:
    digit = n % 10
    if digit < smallest_digit:
        smallest_digit = digit
    n //= 10

print(smallest_digit)