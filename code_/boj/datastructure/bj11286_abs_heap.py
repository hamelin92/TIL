import sys
import heapq

N = int(sys.stdin.readline())
arr = []
inputs = [int(sys.stdin.readline()) for _ in range(N)]
for x in inputs:
    if x == 0:
        if arr:
            print(heapq.heappop(arr)[1])
        else:
            print(0)
    else:
        heapq.heappush(arr, (abs(x), x))
