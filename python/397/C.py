n = int(input())
A = list(map(int, input().split()))

N = [-1] * n
dup_map = {}
not_dup = n

for i in range(len(A)):
    a= A[i]
    if N[a - 1] == -1:
        N[a - 1] = i
    else:    
        if a not in dup_map:
            not_dup -= 2
            dup_map[a] = [N[a - 1], i]
        else:
            not_dup -= 1
            dup_map[a][1] = i

value_list = [0] * n

for item in dup_map.items():
    i, j = item[1]
    for k in range(i, j):
        value_list[k] += 1

print(max(value_list) * 2 + not_dup + len(dup_map.items()) - max(value_list))