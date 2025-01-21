from itertools import accumulate

N, S = map(int, input().split())
A = list(map(int, input().split()))

total_sum = sum(A)
S %= total_sum

A.extend(A)

prefix_sum = set(accumulate(A, initial=0))

for p in prefix_sum:
  if p + S in prefix_sum:
    print("Yes")
    exit()

print("No")
