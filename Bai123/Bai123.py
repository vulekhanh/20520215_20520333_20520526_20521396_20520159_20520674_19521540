
at = 2
bt = 1
n = int(input("Nhập giá trị n: "))


if n < 2:
    print("Vui lòng nhập n không nhỏ hơn 2.")
else:
    for i in range(2, n + 1):
        ahh = 3 * bt + 2 * at
        bhh = at + 3 * bt
        at = ahh
        bt = bhh

    print(f"Số hạng thứ {n} của dãy a là: {at}")
    print(f"Số hạng thứ {n} của dãy b là: {bt}")

