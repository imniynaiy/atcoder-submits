N, S = map(int, input().split())
A = [int(num) for num in input().split()]
totalA = sum(A)
N2 = S % totalA

result = "No"
for i in range(N):
    cur = A[i]
    # print(i,cur)
    if cur == N2:
        result = "Yes"
        break
    for j in range(i+1,N):
        cur += A[j]
        # print(i,j,cur)
        if cur == N2:
            result = "Yes"
            break
 
print(result)