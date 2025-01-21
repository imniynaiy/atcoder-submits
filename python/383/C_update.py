H,W,D= map(int, input().split())
S = [input() for _ in range(H)]
ds = [[-1] * W for _ in range(H)]
from collections import deque
Q = deque()

for i in range(H):
    for j in range(W):
        if S[i][j] == "H":
            Q.append((i,j))
            ds[i][j] = 0
sum = 0
dh = (-1, 0, 1, 0)
dw = (0, -1, 0, 1)
while Q:
    (i,j) = Q.popleft()
    for d in range(4):
        nh = i + dh[d]
        nw = j + dw[d]
        if nh < 0 or nw < 0:
            continue
        if nh >= H or nw >= W:
            continue
        if S[nh][nw] == '#':
            continue
        if ds[nh][nw] != -1:
            continue
        ds[nh][nw] = ds[i][j] + 1
        Q.append((nh, nw))

for i in range(H):
    for j in range(W):
        if ds[i][j] == -1:
            continue
        if ds[i][j] > D:
            continue
        sum += 1
# for i in range(H):
#     print(S[i])
print(sum)
    

            
                
                

