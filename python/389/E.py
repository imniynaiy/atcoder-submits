import math

N, M = map(int, input().split())

P = [int(num) for num in input().split()]

P.sort()
i = 0

sum = 0

while M > 0:
    if i > len(P) - 2:
        break
    cur = P[i]
    next = P[i+1]
    i += 1
    max_cur_k = math.floor(math.sqrt(M/cur))
    if max_cur_k == 0:
        break

    if max_cur_k * max_cur_k > next:
        max_cur_k = math.floor(math.sqrt(next))
    
    sum += max_cur_k
    M -= cur * max_cur_k * max_cur_k

cur = P[i]
max_cur_k = math.floor(math.sqrt(M/cur))
sum += max_cur_k

print(sum)