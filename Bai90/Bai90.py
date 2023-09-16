x = int(input("x: "))
n = int(input("n: "))

s=0
t=1
m=1
i=1
dau = -1

while i<=n:
    t = t*x
    m = m*i
    s+= dau*t/m
    i+=1
    dau = -dau

print(s)

