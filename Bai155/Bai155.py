n = int(input("Nhập giá trị n: "))

if n >= 0:
    t = 1
    i = 0

    print(f"Dãy giá trị a0, a1, a2, ..., an:")
    while i <= n:
        ai = 2 ** (i + 1)
        print(f"a{i} = {ai}")
        i += 1
else:
    print("Vui lòng nhập n lớn hơn hoặc bằng 0.")

