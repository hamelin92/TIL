import sys


def delete_min(v_set, arr):
    min_el = -1
    for i in v_set:
        if min_el < 0:
            min_el = i
            continue
        if arr[i] < arr[min_el]:
            min_el = i
    return min_el


def djikstra(G: list, V: set, start, end, n: int):
    costs = [100000001]*(n+1)
    S = {start}
    costs[start] = 0
    for u in V-S:
        if G[start][u] < 100000001:
            costs[u] = G[start][u]
    while len(S) < n:
        u = delete_min(V-S, costs)
        S = S|{u}
        for j in range(1, n+1):
            if G[u][j] < 100000001 and set([j]).issubset(V-S) and costs[u] + G[u][j] < costs[j]:
                costs[j] = costs[u] + G[u][j]
    return costs[end]


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
weighted_nodes = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
start, end = map(int, sys.stdin.readline().split())
graph = [[100000001]*(N+1) for _ in range(N+1)]
for w in weighted_nodes:
    graph[w[0]][w[1]] = min(graph[w[0]][w[1]], w[2])
cities = set(range(1, N+1))
print(djikstra(graph, cities, start, end, N))
