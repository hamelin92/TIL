from collections import deque, defaultdict
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
islands = defaultdict(list)
visited = [[0]*M for _ in range(N)]
k = 1
for i in range(N):
	for j in range(M):
		if visited[i][j] == 0:
			visited[i][j] += 1
			if arr[i][j] == 1:
				que = deque([(i,j)])
				arr[i][j] = k
				while que:
					flag = 0
					q = que.popleft()
					for d in range(4):
						ni = q[0] + di[d]
						nj = q[1] + dj[d]
						if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0 and arr[ni][nj] == 1:
							que.append((ni,nj))
							visited[ni][nj] += 1
							arr[ni][nj] = k
						elif 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
							flag = 1
					if flag == 1:
						islands[k].append(q)
				k += 1
adj = [[0]*(k-1) for _ in range(k-1)]

for num in islands.keys():
	for s in islands[num]:
		start = arr[s[0]][s[1]]-1
		for d in range(4):
			i = 1
			while True:
				si = s[0] + i*di[d]
				sj = s[1] + i*dj[d]
				if 0 <= si < N and 0 <= sj < M and arr[si][sj] == 0:
					i += 1
				elif 0 <= si < N and 0 <= sj < M and arr[si][sj] != start+1:
					v = arr[si][sj] -1
					if 2 < i and (adj[start][v] == 0 or adj[start][v] > i-1):
						adj[start][v] = i - 1
						adj[v][start] = i - 1
					else:
						break
				else:
					break

span = [0]
answer = 0
while len(span) < k-1:
	min_len = N+M
	a = b = k
	for s in span:
		for j in range(k-1):
			if s != j and j not in span:
				if 0 < adj[s][j] < min_len:
					min_len = adj[s][j]
					a, b = s, j
	if a >= k-1 or b >= k-1:
		break
	span.append(b)
	answer += adj[a][b]
	if min_len == N+M:
		break
if len(span) == k-1:
	print(answer)
else:
	print(-1)