import math


n = int(input())
s = input()

pos1 = []
sum = 0

for i in range(n):
    if s[i] == '1':
        pos1.append(i)
        sum += i

count1 = len(pos1)
center = sum / count1

min = 10e100

for i in range(-count1, count1, 1):
    start = math.ceil(center + i)
    # print(start)
    ans = 0

    for j in range(count1):
        ans += abs(pos1[j] - start - j)
    if ans < min:
        min = ans
    # print(ans)



print(min)