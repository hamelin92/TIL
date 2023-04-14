import sys
import heapq
N, K = map(int, sys.stdin.readline().split())
jewels = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
bags = [int(sys.stdin.readline()) for _ in range(K)]
jewels.sort(key=lambda x: x[1], reverse=True)
heapq.heapify(bags)
ans = 0
for j in jewels:
    b = 0
    while b < len(bags) and bags[b] < j[0]:
        b = 2*(b+1)
    if b < len(bags) and bags[b] >= j[0]:
        bags.pop(b)
        ans += j[1]
        heapq.heapify(bags)

print(ans)