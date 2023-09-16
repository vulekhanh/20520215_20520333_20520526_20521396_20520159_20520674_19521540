n = int(input("Nhập n: "))
t = 1

if n <= 0:
    print("Vui lòng nhập một số nguyên dương.")
else:
    for i in range(1, n + 1):
        if n % i == 0:
            t *= i
    print(f"Tích các ước của {n}: {t}")





