import sys
from collections import defaultdict

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
max_cost = n*100000 + 1
bus = defaultdict(list)
for _ in range(m):
    s, e, w = map(int, sys.stdin.readline().split())
    bus[s].append((e, w))
start, end = map(int, sys.stdin.readline().split())
cities = set(range(1, n+1))
costs = [max_cost]*(n+1)
visit = [()] * (n+1)
costs[start] = 0
visit[start] = [start]
cities.remove(start)
for g in bus[start]:
    if g[1] < costs[g[0]]:
        visit[g[0]] = (start, g[0])
        costs[g[0]] = g[1]
while cities:
    d = min(cities, key=lambda x: costs[x])
    cities.remove(d)
    for g in bus[d]:
        if g[0] in cities and costs[d] + g[1] < costs[g[0]]:
            visit[g[0]] = (*visit[d], g[0])
            costs[g[0]] = costs[d] + g[1]
print(costs[end])
print(len(visit[end]))
print(*visit[end])
