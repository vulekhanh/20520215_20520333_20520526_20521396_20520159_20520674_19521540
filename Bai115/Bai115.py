
att = -1
at = 3
n = int(input("Nhập giá trị n: "))


if n < 0:
    print("Vui lòng nhập n không nhỏ hơn 0.")
else:
    if n == 0:
        result = att  
    elif n == 1:
        result = at   
    else:
        i = 2
        while i <= n:
            ahh = 5 * at + 6 * att
            att = at
            at = ahh
            i += 1
            result = att 

    print(f"Phần tử thứ {n} của dãy là: {result}")

