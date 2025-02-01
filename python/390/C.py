H, W = map(int, input().split())
S = []
for i in range(H):
    S.append(input())

left_edge = 1000
right_edge = -1
top_edge = 1000
bottom_edge = -1

for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            if top_edge == 1000:
                top_edge = i
            if j < left_edge:
                left_edge = j
            if j > right_edge:
                right_edge = j
            bottom_edge = i

for i in range(top_edge, bottom_edge+1):
    for j in range(left_edge, right_edge+1):
        # print(i,j)
        if S[i][j] == ".":
            print("No")
            exit()

if top_edge == 1000:
    print("No")
    exit()

print("Yes")