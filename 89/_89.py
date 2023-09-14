x = float(input("x: "))
n = int(input("n: "))

s = 0
s2 = 0
for i in range(1, n + 1):
    s2 += i
    s = (-1) ** i * x**i / s2

print(s)
