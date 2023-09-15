import math
s=1
t=1
m=1
i=2
x = float(input("Nhập giá trị x: "))
n = int(input("Nhập giá trị n: "))
if(n<=0):
  print(f"Vui lòng nhấp số nguyên dương")
else:
    
    while (i<=2*n):
       t = t*x*x
       m = m*i*(i-1)
       s = s + t/m
       i = i + 2
    print(f"S({x}, {n}) = {s}")

