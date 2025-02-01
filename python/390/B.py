N = int(input())

A = [int(num) for num in input().split()]

k = A[1] / A[0]
prev = A[0]

for i,a in enumerate(A[1:]):
    if a == k * prev:
        prev = a
        continue
    else:
        print("No")
        exit()

print("Yes")