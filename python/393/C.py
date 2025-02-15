n,m = map(int, input().split())

mat = [[False for _ in range(n)] for _ in range(n)]

count = 0

for i in range(m):
    a,b = map(int, input().split())
    if a > b:
        a,b = b,a
    if a == b:
        count += 1
    elif mat[a-1][b-1]:
        count += 1
    else:
        mat[a-1][b-1] = True

print(count)

