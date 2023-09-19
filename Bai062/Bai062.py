
n = float(input("Nhap n: "))
s = 0

while(n > 0 ):
    i = n% 10
    if (i%2==0):
        s = s+i
    n = n//10

print ("Tong cac chu so chan cua n: ", s)
