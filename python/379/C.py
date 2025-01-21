N, M = map(int, input().split())
X = [int(num) for num in input().split()]
A = [int(num) for num in input().split()]

merged = sorted(zip(X, A), key=lambda pair: pair[0])

count =  0
if merged[0][0] != 1:
    print(-1)
    exit()
    
for i in range(M-1):
    to_move = merged[i+1][0] - merged[i][0] - 1
    extra = merged[i][1] - (merged[i+1][0] - merged[i][0])
    steps = to_move * (to_move + 1) / 2  + (to_move+1) * extra
    count += int(steps)
    if (extra < 0):
        print(-1)
        exit()
    merged[i+1] = (merged[i+1][0], merged[i+1][1] + extra)

to_move = N - merged[M-1][0]
extra = merged[M-1][1] - (N - merged[M-1][0]) - 1
steps = to_move * (to_move + 1) / 2  + to_move * extra
count += int(steps)
if (extra != 0):
    print(-1)
    exit()
print(int(count))
