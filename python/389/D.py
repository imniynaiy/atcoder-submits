import math

R = int(input())

if R == 1:
    print(1)
    exit()

i, j = 0,0

limit = R * R - 0.5

j = 1e7
sum = 0

while j > 0:
    x = limit - i * i - i
    if 1 + 4 * x < 0:
        break
    j = (math.sqrt(1 + 4 * x) - 1) / 2
    # print("i,j: ",i,j)
    if (j - math.floor(j) == 0):
        print("!")
    j = math.floor(j)
    i += 1
    if i == 0 or j == 0:
        sum += 2 * j
    else:
        sum += 4 * j

print(sum+1)
