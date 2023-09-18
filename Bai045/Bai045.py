import math
n=float(input("Nhap n: "))
s=1
i=1
while (i<=n):
    s+=1/(math.sqrt(i)+math.sqrt(i+1))
    i+=1
print("S(n) = " , s)


