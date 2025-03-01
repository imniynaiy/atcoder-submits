n = int(input())

A = list(map(int, input().split()))

AwithIndex = [(A[i], i) for i in range(n)]

AwithIndex.sort()

last = AwithIndex[0]
cur_dif = 9e9
for i in range(1,n):
    if last[0] == AwithIndex[i][0]:
        new_dif = AwithIndex[i][1] - last[1]
        if new_dif < cur_dif:
            cur_dif = new_dif
    last = AwithIndex[i]

if cur_dif == 9e9:
    print(-1)
else:
    print(cur_dif + 1)