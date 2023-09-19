from math import sin

x = int(input("x: "))
n = int(input("n: "))

s=0
t=1
i=1

while i<=n:
    t = t*sin(x)
    s+= t
    i+=1

print(s)

