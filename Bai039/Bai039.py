n = int(input("Nhap n: "))
s = 0
i = 1
t=1

while(i<=n):
    t = t*(1+1/(i*i))
    i = i + 1
print(t)
