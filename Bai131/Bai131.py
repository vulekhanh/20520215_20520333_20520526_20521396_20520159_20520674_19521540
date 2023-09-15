import math

def is_triangle(xA, yA, xB, yB, xC, yC):
    a = math.sqrt((xB - xA)**2 + (yB - yA)**2)
    b = math.sqrt((xC - xA)**2 + (yC - yA)**2)
    c = math.sqrt((xC - xB)**2 + (yC - yB)**2)

    if a + b > c and b + c > a and c + a > b:
        return True
    else:
        return False

xA = float(input("Nhập xA: "))
yA = float(input("Nhập yA: "))
xB = float(input("Nhập xB: "))
yB = float(input("Nhập yB: "))
xC = float(input("Nhập xC: "))
yC = float(input("Nhập yC: "))

if is_triangle(xA, yA, xB, yB, xC, yC):
    print("Ba điểm tạo thành một tam giác.")
else:
    print("Ba điểm không tạo thành một tam giác.")

