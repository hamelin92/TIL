import sys
import heapq

N = int(sys.stdin.readline())
hp = []
ops = [int(sys.stdin.readline()) for _ in range(N)]
for x in ops:
    if x == 0:
        if not hp:
            print(0)
        else:
            print(-heapq.heappop(hp))
    else:
        heapq.heappush(hp, -x)
