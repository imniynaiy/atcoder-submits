n,m = map(int, input().split())

A = [int(num) for num in input().split()]

A.sort()

B = []

k = 0

for i in range(1,n+1):
    if k < m:
        if i < A[k]:
            B.append(i)
        elif i == A[k]:
            k += 1
    else:
        B.append(i)
string_result = " ".join(map(str, B))
print(len(B))
print(string_result)