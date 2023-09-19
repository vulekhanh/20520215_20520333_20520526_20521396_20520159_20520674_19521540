n=int(input("Nhap so nguyen duong n: "))
k=0
while (2**k<n):
    k+=1
print("So nguyen k lon nhat sao cho 2^k < n la: ", k-1)
