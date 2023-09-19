from math import pi, sin


n = int(input("n: "))
r = float(input("r: "))

area = ((n * r**2) * sin(2 * pi / n)) / 2

print(area)
