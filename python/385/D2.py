N, M = map(int, input().split())

board = [[' ' for _ in range(N)] for _ in range(N)]

def printboard(b, x, y, color):
    if b[x][y] == ' ':
        b[x][y] = color
    elif b[x][y] == color:
        return
    else:
        print("No")
        exit()

for i in range(M):
    X, Y, color = input().split()
    x = int(X) - 1
    y = int(Y) - 1
    if color == 'B':
        for i in range(x):
            for j in range(y):
                printboard(board,i,j, 'B')
    if color == 'W':
        for i in range(x,N-1):
            for j in (y, N-1):
                printboard(board,i,j, 'W')

print("Yes")
