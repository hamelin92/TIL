import sys

def find(parent, b):
    if parent[b] == b:
        return b
    parent[b] = find(parent, parent[b])
    return parent[b]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def kruskal():
    edges.sort(key=lambda x: x[0])
    cost = 0
    for e in edges:
        if find(parent, e[1]) != find(parent, e[2]):
            cost += e[0]
            union(parent, e[1], e[2])
    return cost


N = int(sys.stdin.readline())
planets = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
planet_idx = list(range(N))
parent = [i for i in range(N)]
edges = []
for i in range(3):
    planet_idx.sort(key=lambda x: planets[x][i])
    edge_i = [(abs(planets[planet_idx[k+1]][i]-planets[planet_idx[k]][i]), planet_idx[k+1], planet_idx[k]) for k in range(N-1)]
    edges.extend(edge_i)
print(kruskal())

