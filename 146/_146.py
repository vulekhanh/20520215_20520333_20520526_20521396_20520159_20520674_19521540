n = int(input("n: "))

reversed_n = 0
temp_n = n
while temp_n != 0:
    reversed_n = reversed_n * 10 + temp_n % 10
    temp_n //= 10

if n == reversed_n:
    print("Is palindrum")
else:
    print("Is not palindrum")
