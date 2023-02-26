from collections import deque

N, K = map(int, input().split())
moves = [lambda x: x-1, lambda x: x+1, lambda x: x<<1]
que = deque([N])
visit = [0]*200001
ans = 0
visit[N] = 1
if N == K:
    ans += 1
while que:
    q = que.popleft()
    for k in range(3):
        nx = moves[k](q)
        if 0 <= nx < 200001 and (not visit[nx] or visit[nx] == visit[q] + 1):
            que.append(nx)
            visit[nx] = visit[q] + 1
            if nx == K:
                ans += 1
print(visit[K]-1)
print(ans)