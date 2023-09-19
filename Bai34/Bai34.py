n = int(input("n: "))

s = 0
i = 1
while i<= 2*n+2:
    s+= i / (i+1)
    i+=2

print(s)

