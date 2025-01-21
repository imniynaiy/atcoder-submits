from atcoder.fenwicktree import FenwickTree

N, Q = map(int, input().split())
a = list(map(int, input().split()))

ft = FenwickTree(N)
for i, el in enumerate(a):
    ft.add(i, el)

for _ in range(Q):
    t, a, b = map(int, input().split())
    if t == 0:
        ft.add(a, b)
    elif t == 1:
        print(ft.sum(a, b))