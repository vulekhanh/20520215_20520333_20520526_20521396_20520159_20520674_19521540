n = int(input("n: "))

s = 0
for i in range(1, n):
    if n % i == 0:
        s += i

print(s)
