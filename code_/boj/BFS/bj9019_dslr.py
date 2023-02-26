import sys
from collections import deque

def dslr(x):
    return map(lambda x: x%10000, (x<<1, x-1, x*10 + x//1000, x//10 + (x%10)*1000))

ds = dslr

dslr_str = ["D", "S", "L", "R"]
T = int(sys.stdin.readline())
for t in range(T):
    A, B = map(int, sys.stdin.readline().split())
    visit = [False]*10000
    visit_info = [False]*10000
    start = A
    visit[A] = -1
    que = deque([start])
    while que:
        q = que.popleft()
        if q == B:
            break
        for k in enumerate(ds(q)):
            nval = k[1]
            if not visit[nval]:
                visit[nval] = q
                visit_info[nval] = dslr_str[k[0]]
                que.append(nval)
    ans = []
    while visit[q] >=0:
        before = visit[q]
        ans.append(visit_info[q])
        q = before
    print(*ans[::-1], sep="")
