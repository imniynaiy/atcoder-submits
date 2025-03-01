n = int(input())
a = list(map(int, input().split()))

last = a[0]

for i in range(1,n):
    if a[i] <= last:
        print("No")
        exit()
    last = a[i]

print("Yes")