import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(N):
    que = deque()
    for j in range(N):
        if graph[i][j]:
            que.append(j)
    while que:
        q = que.popleft()
        for k in range(N):
            if graph[q][k] and not graph[i][k]:
                que.append(k)
                graph[i][k] = 1
for i in range(N):
    print(*graph[i])
