
import math
n = int(input("Nhap n: "))
t = n
lc = n%10
dem = 0
while (t!=0):
    dv = t%10
    if(dv > lc):
        lc = dv
    t = t//10
t = n
while (t!=0):
    dv = t%10
    if(dv == lc):
        dem= dem+1
    t = t//10
print("Chu so lon nhat la ", lc, " va so luong cua no la  ", dem)
