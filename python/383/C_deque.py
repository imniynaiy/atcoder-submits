H,W,D= map(int, input().split())
S = [list(input()) for _ in range(H)]

from collections import deque
Q = deque()

for i in range(H):
    for j in range(W):
        if S[i][j] == "H":
            Q.append((i,j))

sum = 0
# for d in range(1,D+1):
#     while Q:
#         (i,j) = Q.popleft()
#         if (i - 1) >= 0 and S[i-1][j] == '.':
#             S[i-1][j] = d
#             Q.append((i-1,j))
#         if (i + 1) < H and S[i+1][j] == '.':
#             S[i+1][j] = d
#             Q.append((i+1,j))
#         if (j - 1) >= 0 and S[i][j-1] == '.':
#             S[i][j-1] = d
#             Q.append((i,j-1))
#         if (j + 1) < W and S[i][j+1] == '.':
#             S[i][j+1] = d
#             Q.append((i,j+1))


# for i in range(H):
#     for j in range(W):
#         if S[i][j] != '.' and S[i][j] != '#':
#             sum += 1
# # for i in range(H):
# #     print(S[i])
# print(sum)
    

            
                
                

