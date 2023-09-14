n = int(input("n: "))

s = 0
m = 0
for i in range(1, n + 1):
    m += i
    e = 1 / m
    s += e
    if e < 1e-7:
        break

print(s)