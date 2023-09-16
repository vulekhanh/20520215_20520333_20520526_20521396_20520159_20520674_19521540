
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
if a > b:
    temp = a
    a = b
    b = temp
print(a,b)