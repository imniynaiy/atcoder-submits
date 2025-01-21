N, S = map(int, input().split())
A = [int(num) for num in input().split()]
totalA = sum(A)
N2 = S % totalA

# Sliding window approach
result = "No"

current_sum = 0
start = 0

for end in range(N):
    current_sum += A[end]
    
    # Shrink the window from the left if the sum exceeds N2
    while current_sum > N2 and start <= end:
        current_sum -= A[start]
        start += 1
    
    # Check if the current sum matches N2
    if current_sum == N2:
        result = "Yes"
        break

if N2 == 0:
    result = "Yes"

print(result)