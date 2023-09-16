n = int(input("n: "))

flag = 1
t=n

while t > 1:
    du=t%5
    if du != 0:
        flag = 0
    t= t/5

if flag==1:
    print("La dang")
else:
    print("Ko la dang")

