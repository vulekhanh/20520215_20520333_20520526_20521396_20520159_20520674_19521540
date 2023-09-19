import math
n = int(input("Nhập n: "))
s = 0
i = 1
if n <= 0:
    print("Vui lòng nhập một số nguyên dương.")
else:
    for i in range(1, n + 1):
        s= s+ math.sqrt(1+1/i**2+1/(i+1)**2) 
    print(f"S(n): ",round(s,2) )
