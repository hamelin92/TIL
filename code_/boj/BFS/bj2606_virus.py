import sys
from collections import deque

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
network = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    u, v = map(int, sys.stdin.readline().split())
    network[u][v] = 1
    network[v][u] = 1
ans = 0
infected = [0]*(N+1)
infected[1] = 1
que = deque([1])
while que:
    q = que.popleft()
    for k in range(1, N+1):
        if network[q][k] and not infected[k]:
            ans += 1
            que.append(k)
            infected[k] = 1
print(ans)
