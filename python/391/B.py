

N,M = map(int, input().split())
S = []
T = []
for i in range(N):
    S.append(input())

for i in range(M):
    T.append(input())

def check(a,b):
    for i in range(M):
        for j in range(M):
            if S[a+i-1][b+j-1] != T[i][j]:
                return False
    return True

next = False
lastJ = -1
lastI = -1

for a in range(1,N-M+2):
    for b in range(1,N-M+2):
        # print(f"a: {a}, b: {b}")
        same = check(a,b)
        if same:
            print(f"{a} {b}")
            exit()