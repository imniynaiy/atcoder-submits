A = [int(num) for num in input().split()]

count = 0
w = []

for i,a in enumerate(A):
    if a != i + 1:
        count += 1
        w.append(i)
ans = "No"

if count == 2 and w[0] + 1 == w[1]:
    ans = "Yes"
    

print(ans)