import sys
from collections import deque

T = int(sys.stdin.readline())
for tc in range(T):
    N, M = map(int, sys.stdin.readline().split())
    docs_priority = list(enumerate(map(int, sys.stdin.readline().split())))
    cnt = 0
    que = deque(docs_priority)
    while que:
        q = que.popleft()
        if q[1] >= max(que, key=lambda x: x[1], default=(0, 0))[1]:
            cnt += 1
            if q[0] == M:
                break
        else:
            que.append(q)
    print(cnt)
