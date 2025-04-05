n, m = map(int, input().split())

x = 0

for i in range(0, m+1):
    x += n ** i
    if x > 10**9:
        print("inf")
        exit()

print(x)