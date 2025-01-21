X = int(input())

list = []

for i in range(1,10):
    for j in range(1,10):
        list.append(i*j)

sum = 0

for n in list:
    if n != X:
        sum += n

print(sum)