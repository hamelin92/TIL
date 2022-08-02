import heapq

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
heapq.heapify(a)
for com in range(m):
	a_1 = heapq.heappop(a)
	a_2 = heapq.heappop(a)
	na = a_1 + a_2
	heapq.heappush(a, na)
	heapq.heappush(a, na)
print(sum(a))