import math

N, M = map(int, input().split())

P = [int(num) for num in input().split()]

P.sort()

for i in range(15):
    P_k = [p * (2 *i+1) for p in P]
    print(P_k)