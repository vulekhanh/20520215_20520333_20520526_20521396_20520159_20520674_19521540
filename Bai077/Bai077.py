import math
n = int(input("Nhap n: "))
k = int(input("Nhap k: "))
s = 0
for i in range(n):
    s = s + math.pow(i + 1,k)
print("Ket qua: ", s)