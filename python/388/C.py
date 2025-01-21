N = int(input())

A = [int(num) for num in input().split()]

def find_biggest_smaller_or_equal(arr, start, target):
    while arr[start] <= target:
        start += 1
    return start
        

count = 0
temp = 0

for a in A:
    half = a // 2
    
    temp = find_biggest_smaller_or_equal(A,temp, half)
    # print(a, temp)
    count += temp

print(count)
