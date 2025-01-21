N, M = map(int, input().split())
X = [int(num) for num in input().split()]
A = [int(num) for num in input().split()]
count =  0
if X[0] != 1:
    print(-1)
    exit()

i = 0
cur = 0
while (cur < N):
    