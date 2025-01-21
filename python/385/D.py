N, M = map(int, input().split())

w_black_max = {}
w_white_min = {}
h_black_max = {}
h_white_min = {}


for i in range(M):
    X, Y, color = input().split()
    x = int(X)
    y = int(Y)
    if color == 'B':
        if y in w_black_max:
            if x > w_black_max[y]:
                print("No")
                exit()
        if x in h_black_max:
            if y > h_black_max[x]:
                print("No")
                exit()
        h_white_min[x] = y
        w_white_min[y] = x
    elif color == 'W':
        if y in w_white_min:
            if x < w_white_min[y]:
                print("No")
                exit()
        if x in h_white_min:
            if y < h_white_min[x]:
                print("No")
                exit()
        h_black_max[x] = y
        w_black_max[y] = x

print("Yes")