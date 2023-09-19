x = float(input("x: "))
y = float(input("y: "))
z = float(input("z: "))

if x + y > z and x + z > y and y + z > x:
    print("Ton tai")
else:
    print("Khong ton tai")
