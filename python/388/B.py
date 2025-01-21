N,D = map(int, input().split())

data = []

for i in range(N):
    T,L = map(int, input().split())
    data.append((T,L))

for i in range(1,D+1):
    max = -1
    for t,l in data:
        w = (l+i)*t
        if w > max:
            max = w
    print(max)
    


