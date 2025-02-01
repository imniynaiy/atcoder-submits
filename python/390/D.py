N = int(input())

A = [int(num) for num in input().split()]

ans = {}

#into one
ans.add(sum(A))

#no action
for a in A:
    sum = sum ^ a

for i in range(1,N // 2 + 1):
    

print(len(ans))
