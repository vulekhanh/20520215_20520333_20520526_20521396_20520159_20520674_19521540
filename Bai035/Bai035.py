import math
n = int(input("Nhập n: "))
t = 1
i = 1
if n <= 0:
    print("Vui lòng nhập một số nguyên dương.")
else:
    for i in range(1, n + 1):
        t =t*i
    print(f"Tích của các số từ 1 đến {n} là {t}")



