a = float(input("Nhập giá trị của a: "))
b = float(input("Nhập giá trị của b: "))

if a == 0:
    if b == 0:
        print("Phương trình vô số nghiệm.")
    else:
        print("Phương trình vô nghiệm.")
else:
    x = -b / a
    print(f"Nghiệm của phương trình là x = {x}")

