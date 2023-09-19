n = int(input("n: "))

a1 = a = n
for i in range(2, n + 1):
    if a1 % 2 == 0:
        a = a1 / 2
    else:
        a = 3 * a1 + 1
    a1 = a

print(a)
