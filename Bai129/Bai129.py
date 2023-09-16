a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

if a>b:
    temp = a
    a = b
    b= temp

if a>c:
    temp = a
    a = c
    c= temp

if b>c:
    temp = b
    b = c
    c= temp


print(f"{a} {b} {c}")

