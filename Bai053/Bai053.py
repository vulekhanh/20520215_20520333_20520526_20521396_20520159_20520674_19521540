n = int(input("Nhap n: "))
count = 0
for i in range(1, n + 1):
    if n % i == 0 and i % 2 == 1:
        count = count + 1
print("So luong uoc le: ", count)
