def main():
    n = int(input())
    a = list(map(int, input().split()))

    suml = [0] * n
    sumr = [0] * n
    vis = [0] * (n + 1)

    now = 0
    for i in range(n):
        if not vis[a[i]]:
            now += 1
        vis[a[i]] = 1
        suml[i] = now

    now = 0
    vis = [0] * (n + 1)
    
    for i in range(n - 1, -1, -1):
        if not vis[a[i]]:
            now += 1
        vis[a[i]] = 1
        sumr[i] = now

    ans = 0
    for i in range(n - 1):
        ans = max(ans, suml[i] + sumr[i + 1])

    print(ans)

if __name__ == "__main__":
    main()