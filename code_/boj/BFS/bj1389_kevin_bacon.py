import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
rel = [[0]*(N+1) for _ in range(N+1)]
for r in range(M):
    A, B = map(int, sys.stdin.readline().split())
    rel[A][B] = 1
    rel[B][A] = 1
ans = 0
min_kbn = N*N
for k in range(1, N+1):
    visit = [0]*(N+1)
    que = deque([k])
    visit[k] = 1
    while que:
        q = que.popleft()
        for i in range(1, N+1):
            if rel[q][i] and not visit[i]:
                que.append(i)
                visit[i] = visit[q] + rel[q][i]
    kkb = sum(visit)-N 
    if min_kbn > kkb:
        ans = k
        min_kbn = kkb
print(ans)
