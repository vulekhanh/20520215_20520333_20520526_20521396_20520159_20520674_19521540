
n = int(input("n: "))

s=0
i=1

while i<n:
    if n%i==0:
        s+= i
    i+=1

if s==n:
    print("HT")
else:
    print("Ko HT")
