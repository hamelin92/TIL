import sys
from collections import deque

N, M =map(int, sys.stdin.readline().split())
sl = dict(map(int, sys.stdin.readline().split()) for _ in range(N+M))
board = list(range(101))
visit = [False]*101
que = deque([1])
while que:
    q = que.popleft()
    if q == 100:
        break
    for k in range(1, 7):
        nq = q+k
        if sl.get(nq) is not None:
            nq = sl.get(nq)
        if nq <= 100 and not visit[nq]:
            que.append(nq)
            visit[nq] = visit[q] + 1
print(visit[q])
