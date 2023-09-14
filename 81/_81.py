x = int(input("x: "))
n = int(input("n: "))

s = 0
s2 = 1
for i in range(0, n + 1):
    s2 *= x + i
    s += 1 / s2

print(s)
