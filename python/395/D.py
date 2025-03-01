n, q = map(int, input().split())

BN = [i for i in range(1, n+1)]

NB = {}

for i in range(1, n+1):
    NB[i] = [i]

for i in range(q):
    inputs = list(map(int, input().split()))
    if inputs[0] == 1:
        a, b = inputs[1], inputs[2]
        BN[a-1] = b
        NB[b].append(a)
    elif inputs[0] == 2:
        a, b = inputs[1], inputs[2]
        for i in NB[a]:
            BN[i-1] = b
        for i in NB[b]:
            BN[i-1] = a
        NB[a], NB[b] = NB[b], NB[a]
    elif inputs[0] == 3:
        a = inputs[1]
        print(BN[a-1])