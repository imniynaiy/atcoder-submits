n = int(input())
P = [int(num) for num in input().split()]
Q = [int(num) for num in input().split()]

Q_to_i = [0] * n
result = []

for i in range(n):
    q = Q[i]
    Q_to_i[q-1] = i+1

for a in range(n):
    i = Q_to_i[a] - 1
    ii = P[i]
    result.append(Q[ii - 1])

string_result = " ".join(map(str, result))
print(string_result)