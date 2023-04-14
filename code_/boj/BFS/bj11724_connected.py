import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[0]*(N+1) for _ in range(N+1)]
for m in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u][v] = 1
    graph[v][u] = 1
nodes = [0] * (N+1)
ans = 0
for s in range(1, N+1):
    if not nodes[s]:
        ans += 1
        que = deque([s])
        nodes[s] = 1
        while que:
            q = que.popleft()
            for k in range(1, N+1):
                if graph[q][k] and not nodes[k]:
                    que.append(k)
                    nodes[k] = 1
print(ans)