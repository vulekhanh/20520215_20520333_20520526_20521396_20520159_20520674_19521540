n = int(input("Nhập n: "))
dem=0
t=n

if n <= 0:
    print("Vui lòng nhập một số nguyên dương.")
else:
    while t > 0:
            dem+=1
            t=t//10
    print(f"Số chữ số của {n}: {dem}")






