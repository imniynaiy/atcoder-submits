n = int(input())
S = []
for i in range(n):
    S.append(input())

S = sorted(S, key=len)

ans = "".join(S)

print(ans)

