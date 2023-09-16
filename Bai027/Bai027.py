import math
n = int(input("Nhập n: "))
s = 0
i=1
if n <= 0:
    print("Vui lòng nhập một số nguyên dương.")
else:
    for i in range(1, n + 1):
        s += i
    print(f"Tổng của các số từ 1 đến {n} là {s}")


