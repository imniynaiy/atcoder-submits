H,W,D= map(int, input().split())
hu = [[0 for _ in range(W)] for _ in range(H)]
S = ["" for i in range(H)]
floors = []
for i in range(H):
    S[i]=input()
    for j in range(W):
        if S[i][j] == '.':
            floors.append((i,j))

max = 0
for i in range(len(floors)):
    for j in range(i+1,len(floors)):
        (ax, ay) = floors[i]
        (bx, by) = floors[j]
        # if ax == 1 and ay == 3 and bx == 4 and by == 2:
        #     print(i,j, sum)
        for x in range(D+1):
            Y = D - x
            for y in range(Y+1):
                # if ax == 1 and ay == 3 and bx == 4 and by == 2 and (x == 1) and y == 1:
                #     x = x
                if (ax - x) >= 0 and (ay - y) >= 0 and (ax - x) < H and (ay - y) < W and S[ax - x][ay-y] == '.':
                    hu[ax-x ][ay-y] = 1
                if (ax + x) >= 0 and (ay + y) >= 0 and (ax + x) < H and (ay + y) < W and S[ax + x][ay+y] == '.':
                    hu[ax+x][ay+y] = 1
                if (ax - x) >= 0 and (ay + y) >= 0 and (ax - x) < H and (ay + y) < W and S[ax - x][ay+y] == '.':
                    hu[ax-x ][ay+y] = 1
                if (ax + x) >= 0 and (ay - y) >= 0 and (ax + x) < H and (ay - y) < W and S[ax + x][ay-y] == '.':
                    hu[ax+x][ay-y] = 1
                if (bx - x) >= 0 and (by - y) >= 0 and (bx - x) < H and (by - y) < W and S[bx - x][by-y] == '.':
                    hu[bx-x ][by-y] = 1
                if (bx + x) >= 0 and (by + y) >= 0 and (bx + x) < H and (by + y) < W and S[bx + x][by+y] == '.':
                    hu[bx+x][by+y] = 1
                if (bx - x) >= 0 and (by + y) >= 0 and (bx - x) < H and (by + y) < W and S[bx - x][by+y] == '.':
                    hu[bx-x ][by+y] = 1
                if (bx + x) >= 0 and (by - y) >= 0 and (bx + x) < H and (by - y) < W and S[bx + x][by-y] == '.':
                    hu[bx+x][by-y] = 1
        sum = 0
        for x in range(H):
            for y in range(W):
                sum += hu[x][y]

        if sum > max:
            max = sum
        hu = [[0 for _ in range(W)] for _ in range(H)]

print(max)

            
                
                
