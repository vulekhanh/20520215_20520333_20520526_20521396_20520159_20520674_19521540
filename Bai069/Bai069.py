x=float(input("Nhap x: "))
n=int(input("Nhap so mu n: "))
s=0
for i in range(1,n+1):
    s+=x**i  
print("S(n) : ", s)