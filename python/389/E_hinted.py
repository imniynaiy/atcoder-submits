import math

N, M = map(int, input().split())

P = [int(num) for num in input().split()]

P.sort()

max_p_limit = math.ceil(math.sqrt(M)) * 2 + 1
min_p_limit = 0

M_left = M
cur_p_limit = math.floor((max_p_limit + min_p_limit) / 2)
sum = 0

while min_p_limit != max_p_limit:
    M_left = M
    cur_p_limit = math.floor((max_p_limit + min_p_limit) / 2)
    # print("p:[", min_p_limit, max_p_limit, "]")
    # print("cur_limit:", cur_p_limit)
    sum = 0

    max_k = 0

    for p in P:
        if p > cur_p_limit:
            break
        k = math.floor((cur_p_limit/p + 1) / 2)
        # print("p, k: ", p,k)
        M_left -= k*k*p
        # print("M_left: ", M_left)
        sum += k
    # print("M_left: ", M_left)
    
    if M_left > 0:
        min_p_limit = cur_p_limit + 1
    elif M_left < 0:
        max_p_limit = cur_p_limit
    else:
        print(sum)
        exit()

M_left = M
cur_p_limit = math.floor((max_p_limit + min_p_limit) / 2)
# print("final limit of p:", cur_p_limit)
sum = 0

max_k = 0

for i,p in enumerate(P):
    if p > cur_p_limit:
        break
    k = math.floor((cur_p_limit/p) / 2)
    # print("p, k: ", p,k)
    M_left -= k*k*p
    P[i] = (2*k+1) * p
    sum += k

P.sort()

for p in P:
    if M_left < p:
        break
    M_left -= p
    sum += 1
 

print(sum)





