import math
n = float(input("Nhap n: "))
s = 0;
i = 1;
while(i <= n ):
    s = s + math.pow(i, 4)
    i = i+1;
print ("Tong can tinh: ", s)
