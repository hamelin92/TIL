import sys
def delete_min(v_set):
    min_el = -1
    for i in v_set:
        if min_el < 0:
            min_el = i
            continue
        if costs[i] < costs[min_el]:
            min_el = i
    return min_el


N, M, X = map(int, sys.stdin.readline().split())
roads =  [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
graph = [[0] * (N+1) for _ in range(N+1)]
for r in roads:
    graph[r[0]][r[1]] += r[2]
costs = [0]*(N+1)
V = set(range(1, N+1))
V_x = V - {X}
S = {X}
costs[X] = 0
for u in V_x:
    costs[u] = graph[X][u]
while len(S) < N:
    u = delete_min(V-S)
    S = S|{u}
    for j in range(1, N+1):
        if graph[u][j] > 0 and set([j]).issubset(V-S) and costs[u] + graph[u][j] < costs[j]:
            costs[j] = costs[u] + graph[u][j]



