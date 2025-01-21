H, W, D = map(int, input().split())
S = [input() for _ in range(H)]


from collections import deque

Q = deque()
dist = [[-1] * W for _ in range(H)]
for h in range(H):
    for w in range(W):
        if S[h][w] == 'H':
            Q.append((h, w))
            dist[h][w] = 0
dh = (-1, 0, 1, 0)
dw = (0, -1, 0, 1)
while Q:
    h, w = Q.popleft()
    for d in range(4):
        nh = h + dh[d]
        nw = w + dw[d]
        if nh < 0 or nw < 0:
            continue
        if nh >= H or nw >= W:
            continue
        if S[nh][nw] == '#':
            continue
        if dist[nh][nw] != -1:
            continue
        dist[nh][nw] = dist[h][w] + 1
        Q.append((nh, nw))
ans = 0
for h in range(H):
    for w in range(W):
        if dist[h][w] == -1:
            continue
        if dist[h][w] > D:
            continue
        ans += 1
# for d in dist:
#     print(d)
print(ans)
