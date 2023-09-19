
import math
n = float(input("Nhap n: "))
x = float(input("Nhap x: "))
s = 1 -x
t = x 
m = 1
i = 3 
dau = 1
while(i<=(2*n+1)):
    t = t*x*x 
    m = m*i*(i-1)
    s = s + dau*t/m
    i = i+2
   
print ("Tong can tinh: ", s)
