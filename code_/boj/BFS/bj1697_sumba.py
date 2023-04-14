from collections import deque

N, K = map(int, input().split())
visit = [0]*100031
que = deque([N])
visit[N] = 1
while que:
    q = que.popleft()
    if q == K:
        break
    if q-1 >= 0:
        if not visit[q-1]:
            que.append(q-1)
            visit[q-1] = visit[q]+1
        if 2*q < 100030 and not visit[2*q]:
            que.append(2*q)
            visit[2*q] = visit[q]+1
    if q < 100000 and not visit[q+1]:
        que.append(q+1)
        visit[q+1] = visit[q] + 1
print(visit[K]-1)
