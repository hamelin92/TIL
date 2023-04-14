from collections import deque

N = int(input())
que = deque([[N]])
visit = [0]*(N+1)
visit[N] = 1
while que:
    ql = que.popleft()
    q = ql[-1]
    if q == 1:
        break
    if not q%3 and not visit[q//3]:
        nq = q//3
        que.append(ql+[nq])
        visit[nq] = visit[q] + 1
    if not q%2 and not visit[q//2]:
        nq = q//2
        que.append(ql+[nq])
        visit[nq] = visit[q] + 1
    if q > 1 and not visit[q-1]:
        que.append(ql+[q-1])
        visit[q-1] = visit[q] + 1
print(visit[1]-1)
print(*ql)