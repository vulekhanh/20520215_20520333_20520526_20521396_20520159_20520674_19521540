x = float(input("x: "))

if x < 0:
    f = -2 * x**3 + 6 * x + 9
elif x <= 1 and x >= 0:
    f = 5 * x - 7
else:
    f = 2 * x**3 + 5 * x**2 - 8 * x + 3

print(f)
