from collections import deque, defaultdict

m, n = map(int, input().split())
k = int(input())
bus = [list(map(int, input().split())) for _ in range(k)]
sx, sy, dx,dy = map(int, input().split())
graph = defaultdict(list)
for i in range(k):
	for j in range(i+1,k):
		if bus[i][1] <= bus[j][3] and bus[i][3] >= bus[j][1] and bus[i][2] <= bus[j][4] and bus[i][4] >= bus[j][2]:
			graph[i].append(j)
			graph[j].append(i)
start = []
end = set()
for i in range(k):
	if bus[i][1] <= sx <= bus[i][3] and bus[i][2] <= sy <= bus[i][4]:
		start.append([i])
	if bus[i][1] <= dx <= bus[i][3] and bus[i][2] <= dy <= bus[i][4]:
		end.add(i)
que = deque(start)
answer = 0

while que:
	q = que.popleft()
	if q[-1] in end:
		answer = len(q)
		break
	for s in graph[q[-1]]:
		if s not in q:
			que.append(q+[s])
print(answer)
