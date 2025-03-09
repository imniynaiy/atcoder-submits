class Undigraph:
    def __init__(self, v):
        self.vertex = v
        self.edge = 0
        self.adj_list = [[] for _ in range(v)]
        self.weight_list = [[] for _ in range(v)]

    def num_of_vertices(self):
        return self.vertex

    def num_of_edges(self):
        return self.edge

    def add_edge(self, x: int, y: int, w: int):
        """Cuz this is a undirected graph, x -> v equals to v -> x"""
        if y not in self.adj_list[x]:
            self.adj_list[x].append(y)
            self.weight_list[x].append(w)
        if x not in self.adj_list[y]:
            self.adj_list[y].append(x)
            self.weight_list[y].append(w)
        self.edge += 1

    def get_edges_of(self, v):
        return self.adj_list[v]
    
    def get_weight_of(self, x, y):
        if y in self.adj_list[x]:
            return self.weight_list[x][self.adj_list[x].index(y)]
        else:
            return -1

n,m = map(int, input().split())

UG = Undigraph(n)

for _ in range(m):
    x, y, w = map(int, input().split())
    UG.add_edge(x-1, y-1, w)


def findAllPath(graph,start,end):
    path=[]
    stack=[]
    stack.append(start)
    visited=set()
    visited.add(start)
    seen_path={}
    #seen_node=[]
    while (len(stack)>0):
        start=stack[-1]
        nodes=graph.get_edges_of(start)
        if start not in seen_path.keys():
            seen_path[start]=[]     
        g=0
        for w in nodes:
            if w not in visited and w not in seen_path[start]:
                g=g+1
                stack.append(w)
                visited.add(w)
                seen_path[start].append(w)
                if w==end:
                    path.append(list(stack))
                    old_pop=stack.pop()
                    visited.remove(old_pop)
                break    
        if g==0:
            old_pop=stack.pop()
            del seen_path[old_pop]
            visited.remove(old_pop)
    return path

def getXor(path, graph):
    xor = graph.get_weight_of(path[0], path[1])
    for i in range(1, len(path)-1):
        xor = xor ^ graph.get_weight_of(path[i], path[i+1])
    return xor

paths = findAllPath(UG, 0, n-1)
minxor = -1

for path in paths:
    xor = getXor(path, UG)
    if minxor == -1 or xor < minxor:
        minxor = xor

print(minxor)