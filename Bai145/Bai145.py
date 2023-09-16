n = int(input("n: "))

flag = 0
i=0

while i <= n:
    if i*i == n:
        flag = 1
    i+= 1

if flag==1:
    print("La CP")
else:
    print("Ko CP")

