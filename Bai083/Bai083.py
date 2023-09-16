import math

s = 0
t = 1
i = 1

x = float(input("Nhập giá trị x: "))
n = int(input("Nhập giá trị n: "))

if n <= 0:
    print("Vui lòng nhập một số nguyên dương.")
else:
    for i in range(1, n + 1):
        t = t * x
        s = s + math.sin(t)

    print(f"S({x}, {n}) = {s}")
