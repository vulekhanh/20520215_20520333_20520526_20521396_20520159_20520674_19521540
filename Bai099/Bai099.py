import math

s = 0
i = 1

n = int(input("Nhập giá trị n: "))


if n <= 0:
    print("Vui lòng nhập một số nguyên dương.")
else:
    for i in range(1, n + 1):
        s = math.pow(i+s, 1/(i+1))

    print(f"S({n}) = {s}")

