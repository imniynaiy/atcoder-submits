N = int(input())
T,V = map(int, input().split())

for i in range(N-1):
    newT, newV= map(int, input().split())
    leak = newT - T
    if leak > V:
        V = newV
    else:
        V = V - leak + newV
    T = newT

print(V)