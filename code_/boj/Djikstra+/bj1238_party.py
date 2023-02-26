import sys
from pprint import pprint


def delete_min(v_set, arr):
    min_el = -1
    for i in v_set:
        if min_el < 0:
            min_el = i
            continue
        if arr[i] < arr[min_el]:
            min_el = i
    return min_el


def shortest(G, V, start, n):
    costs = [100000000]*(N+1)
    V_x = V - {start}
    S = {start}
    costs[start] = 0
    for u in V_x:
        if G[start][u]:
            costs[u] = G[start][u]
    while len(S) < n:
        u = delete_min(V-S, costs)
        S = S|{u}
        for j in range(1, n+1):
            if G[u][j] > 0 and set([j]).issubset(V-S) and costs[u] + G[u][j] < costs[j]:
                costs[j] = costs[u] + G[u][j]
    return costs


N, M, X = map(int, sys.stdin.readline().split())
roads =  [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
ver = set(range(1, N+1))
graph = [[0] * (N+1) for _ in range(N+1)]
adj = [[0] * (N+1) for _ in range(N+1)]
for r in roads:
    graph[r[0]][r[1]] += r[2]
    adj[r[1]][r[0]] += r[2]
go_party = shortest(graph, ver, X, N)
go_home = shortest(adj, ver, X, N)
print(max([go_home[i]+go_party[i] for i in range(1, N+1)]))
