H,W,D= map(int, input().split())
S = [[] for _ in range(H)]
hus = []
next = []

for i in range(H):
    S[i]=list(input())
    for j in range(W):
        if S[i][j] == "H":
            hus.append((i,j))
sum = 0
for d in range(1,D+1):
    for (i,j) in hus:
        if (i - 1) >= 0 and S[i-1][j] == '.':
            S[i-1][j] = d
            next.append((i-1,j))
        if (i + 1) < H and S[i+1][j] == '.':
            S[i+1][j] = d
            next.append((i+1,j))
        if (j - 1) >= 0 and S[i][j-1] == '.':
            S[i][j-1] = d
            next.append((i,j-1))
        if (j + 1) < W and S[i][j+1] == '.':
            S[i][j+1] = d
            next.append((i,j+1))
    hus = next
    next = []

for i in range(H):
    for j in range(W):
        if S[i][j] != '.' and S[i][j] != '#':
            sum += 1
# for i in range(H):
#     print(S[i])
print(sum)
    

            
                
                

