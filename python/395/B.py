n = int(input())

graph = [["?" for _ in range(n)] for _ in range(n)]

def paint(graph, i, ch):
    for h in range(i,n - i):
        for w in range(i,n - i):
            graph[h][w] = ch
        
for i in range(n):
    if i % 2 == 0:
        ch = "#"
    else:
        ch = "."
    paint(graph, i, ch)

for i in range(n):
    print("".join(graph[i]))