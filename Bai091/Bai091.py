import math

s = -1
t = 1
m = 1
i = 2
dau = 1
n = int(input("Nhập giá trị n: "))
x = float(input("Nhập giá trị x: "))

if n <= 0:
    print("Vui lòng nhập một số nguyên dương.")
else:
    for _ in range(1, n + 1):
        t = t * x * x
        if i > 0:
            m = m * i * (i - 1)
            s = s + dau * t / m
        i = i + 2
        dau = -dau

    print(f"S( {x},{n}) = {s}")
