import math

i = 1043
x = long(1e19)
a = math.floor(1e19 / i)
b = 10e18 // i
while (a == b):
    i += 1
    a = math.floor(1e19 / i)
    b = 1e19 // i

print(a==b, a, b, i)
print(b*i, (b+1)*i, (b+2)*i)