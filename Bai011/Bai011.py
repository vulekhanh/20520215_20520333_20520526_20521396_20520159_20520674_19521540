import math
x1=float(input("x1: "))
y1=float(input("y1: "))
x2=float(input("x2: "))
y2=float(input("y2: "))
x3=float(input("x3: "))
y3=float(input("y3: "))
a=math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))
b=math.sqrt(pow(x3-x2,2)+pow(y3-y2,2))
c=math.sqrt(pow(x3-x1,2)+pow(y3-y1,2))
p=(a+b+c)/2
s=math.sqrt(p*(p-a)*(p-b)*(p-c))
print(f'Dien tich s: ',s)


