x = int(input("Nhap x: "))
y = int(input("Nhap y: "))
n = x
while n <= y:
    if (n%4==0 and n%100!=0) or (n % 400 == 0):
        print(n, end=" ")
    n = n + 1

    
