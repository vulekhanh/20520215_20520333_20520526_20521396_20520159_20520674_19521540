n = int(input("Nhập n: "))
flag = 0
t = n
if n <= 0:
    print("Vui lòng nhập một số nguyên dương.")
else:
    has_odd_digit = False
    while n > 0:
        dv = n % 10
        if dv % 2 != 0:
            has_odd_digit = True
            flag+=1
            break
        n = n // 10

    if has_odd_digit:
        print("Số số lẻ",flag)
        print("Có tồn tại chữ số lẻ.")
    else:
        print("Số số lẻ",flag)
        print("Không tồn tại chữ số lẻ.")


