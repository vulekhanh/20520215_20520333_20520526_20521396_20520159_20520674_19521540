import math
n=int(input("Nhap n dau can: "))
s=0
for i in range (n):
    s=math.sqrt(s+2)
print("S(n) = ", s)