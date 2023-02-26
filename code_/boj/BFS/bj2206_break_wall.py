from collections import deque

N, M = map(int, input().split())
mat = [list(map(int, list(input()))) for _ in range(N)]
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
visit = [[0 for __ in range(M)] for _ in range(N)]
visit2 = [[0 for __ in range(M)] for _ in range(N)]
que = deque([(0, 0, 0)])
visit[0][0] = 1
visit2[0][0] = 1
while que:
    q = que.popleft()
    if q[0] == N-1 and q[1] == M-1:
        break
    for k in range(4):
        ni = q[0] + di[k]
        nj = q[1] + dj[k]
        if 0 <= ni < N and 0 <= nj < M and not visit[ni][nj]:
            if mat[ni][nj] and not q[2] and not visit2[ni][nj]:
                que.append((ni, nj, 1))
                visit2[ni][nj] = visit[q[0]][q[1]]+1
            elif not mat[ni][nj]:
                if not q[2]:
                    que.append((ni, nj, q[2]))
                    visit[ni][nj] = visit[q[0]][q[1]]+1
                    visit2[ni][nj] = visit[q[0]][q[1]] + 1
                elif not visit2[ni][nj]:
                    que.append((ni, nj, q[2]))
                    visit2[ni][nj] = visit2[q[0]][q[1]] + 1
print(max(visit[N-1][M-1], visit2[N-1][M-1]) if visit[N-1][M-1] or visit2[N-1][M-1] else -1)
