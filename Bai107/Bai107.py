import math

x = float(input("Nhập giá trị x (độ): "))
tolerance=1e-6
xx = (x * math.pi) / 180 
s = 1
t = 1
m = 1
dau = -1
e = 1
i = 2


while abs(e) > tolerance:
        t *= xx * xx
        m *= (i - 1) * i
        e = t / m
        s += dau * e
        dau = -dau
        i += 2

print(f"cos({x}) ≈ {s}")
