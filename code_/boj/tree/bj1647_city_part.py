import sys

def find(b):
    if parent[b] != b:
        parent[b] = find(parent[b])
    return parent[b]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def kruskal():
    cost = 0
    max_cost = 0
    for e in edges:
        if find(e[0]) != find(e[1]):
            cost += e[2]
            if e[2] > max_cost:
                max_cost = e[2]
            union(e[0], e[1])
    return (cost, max_cost)

N, M = map(int, sys.stdin.readline().split())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
edges.sort(key=lambda x: x[2])
parent = list(range(N+1))
ans = kruskal()
print(ans[0]-ans[1])
