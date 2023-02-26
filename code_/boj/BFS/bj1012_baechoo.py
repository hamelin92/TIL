import sys
from collections import deque


T = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for t in range(T):
    N, M, K = map(int, sys.stdin.readline().split())
    vegetables = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]
    ground = [[0]*M for _ in range(N)]
    check = [[0]*M for _ in range(N)]
    worms = 0
    for v in vegetables:
        ground[v[0]][v[1]] = 1
    for i in range(N):
        for j in range(M):
            if ground[i][j] and check[i][j] == 0:
                worms += 1
                que = deque([(i, j)])
                while que:
                    q = que.popleft()
                    for k in range(4):
                        ny = q[0] + dy[k]
                        nx = q[1] + dx[k]
                        if 0 <= ny < N and 0 <= nx < M and check[ny][nx] == 0 and ground[ny][nx] == 1:
                            que.append((ny, nx))
                            check[ny][nx] = 1
    print(worms)
