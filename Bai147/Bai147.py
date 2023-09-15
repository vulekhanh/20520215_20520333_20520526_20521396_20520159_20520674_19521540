
n = int(input("Nhập số nguyên dương n: "))


if n == 0:
    print("0")
else:
    flag = 1
    t = n

    while t > 0:
        dv = t % 10
        if dv % 2 == 0:
            flag = 0
            break
        t = t // 10

    if flag == 1:
        print("+1")
        print(f"{n} toàn lẻ.")
    else:
        print("0")
        print(f"{n} không toàn lẻ.")
