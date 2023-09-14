n = int(input("n: "))

a1 = -2
a = a1
pow3 = 1
pow7 = 1
for i in range(2, n + 1):
    pow3 = pow3 * 3
    pow7 = pow7 * 7
    a = 5 * a1 + 2 * pow3 - 6 * pow7 + 12
    a1 = a

print(a)