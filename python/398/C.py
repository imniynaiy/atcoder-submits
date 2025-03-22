n = int(input())

def stoawi(s, i):
    return (int(s), i)

if n == 1:
    print(1)
    exit()

a = list(map(int, input().split()))

awi = [0] * n

for i in range(n):
    awi[i] = stoawi(a[i], i)

awi.sort(reverse=True)

last = awi[0][0]

if last != awi[1][0]:
    print(awi[0][1] + 1)
    exit()

for i in range(1, n):
    cur = awi[i][0]
    if cur == last:
        continue
    elif i == n - 1 or awi[i + 1][0] != cur:
        print(awi[i][1] + 1)
        exit()
    else:
        last = cur

print(-1)
