import math
s = 0
e = 1
i = 1
while e > 0.000001:
    e = 1 / i;
    s = s + e
    i = i + 1
print("Ket qua: ", s)
