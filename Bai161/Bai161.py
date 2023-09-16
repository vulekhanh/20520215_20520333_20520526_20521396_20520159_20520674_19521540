n = int(input("n: "))

flag = 1
t=n

while t >= 10:
    dv=t%10
    hc=(t/10)%10
    if hc>dv:
        flag = 0
    t//=10

if flag==1:
    print("Tang")
else:
    print("Ko tang")

