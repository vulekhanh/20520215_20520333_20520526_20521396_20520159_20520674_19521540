
import math
ab = -1
am = 3 
i=2
n = int(input("Nhap n: "))
while (i <= n):
    aa=5*(2**i)+5*am-ab
    i += 1
    ab=am
    am=aa

print("So hang thu n cua day la ", aa)


