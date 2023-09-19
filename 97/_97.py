from math import sqrt


x = float(input("x: "))
n = int(input("n: "))

s = 0
t = 1
for i in range(1, n + 1):
    t = t * x
    s = sqrt(s + t)

print(s)