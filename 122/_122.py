n = int(input("n: "))

a1 = 1
b1 = 1
a = a1
b = b1
for i in range(2, n + 1):
    a = 3 * b1 + 2 * a1
    b = a1 + 3 * b1
    a1, b1 = a, b

print(f"a = {a}, b = {b}")
