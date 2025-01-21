N = int(input())
A = [int(num) for num in input().split()]

temp = []

for i in range(N):
    to_add,end = 0,0
    if len(temp) > 0:
        to_add, end = temp[len(temp) - 1]
        if i > end:
            temp.pop()
    to_dis = min(A[i]+to_add, N-1-i)
    A[i] += to_add
    A[i] -= to_dis
    temp.append((i+1, i+to_dis))
    # print(i, to_dis, A)

print(' '.join(map(str, A)))
