n = int(input("n: "))

s = 0
for i in range(1, n + 1):
    s += i / (i + 1)

print(s)