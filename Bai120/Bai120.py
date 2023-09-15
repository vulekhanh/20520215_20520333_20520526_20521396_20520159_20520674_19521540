import math
n = int(input("Nhap n: "))
at = 2
i = 2
while i <= n:
    ahh=5*at+math.sqrt(24*pow(at,2)-8)
    i = i + 1
    at=ahh
print(ahh)
