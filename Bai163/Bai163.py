n = int(input("Nhập một số nguyên dương n: "))
t = n  # Lưu lại giá trị ban đầu của n
max_odd_divisor = 1
all_even_divisors = True

if n <= 0:
    print("Vui lòng nhập số nguyên dương lớn hơn 0.")
else:
    while t % 2 == 0:
        t = t // 2
        max_odd_divisor *= 2
        all_even_divisors = True
    
    if t > 1:
        max_odd_divisor = t
        all_even_divisors = False

    if all_even_divisors:
        print(f"+1")
    else:
        print(f"Ước số lẻ lớn nhất của {t} là {max_odd_divisor}.")
