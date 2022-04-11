
from collections import deque
dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

N, M, gas = map(int, input().split())
nav = [list(map(int, input().split())) for _ in range(N)]
R, C = map(int, input().split())
R = R-1
C = C-1
info = [list(map(int, input().split())) for _ in range(M)]
start = set()
end = dict()
for m in range(M):
	start.add((info[m][0]-1,info[m][1]-1))
	end[(info[m][0]-1,info[m][1]-1)] = (info[m][2]-1,info[m][3]-1)
for i in range(M):
	que = deque([(R, C)])
	visit = [[0]*N for _ in range(N)]
	costa = 0
	costb = 0
	while que:
		cases = len(que)
		candidate = []
		for tc in range(cases):
			q = que.popleft()
			if q in start:
				candidate.append(q)
			else:
				for d in range(4):
					nr = q[0] + dr[d]
					nc = q[1] + dc[d]
					if 0 <= nr < N and 0 <= nc < N and visit[nr][nc] == 0 and nav[nr][nc] != 1:
						que.append((nr,nc))
						visit[nr][nc] = visit[q[0]][q[1]] + 1
		if candidate:
			result = candidate[0]
			for client in candidate:
				if client[0] < result[0]:
					result = client
				elif client[0] == result[0] and client[1] < result[1]:
					client = result
			R, C = result[0], result[1]
			target = end[result]
			costa = visit[result[0]][result[1]]
			start -= {result}
			break
	else:
		print(-1)
		break
	que = deque([(R,C)])
	visit = [[0] * N for _ in range(N)]
	while que:
		q = que.popleft()
		if q == target:
			costb = visit[q[0]][q[1]]
			R,C = q[0], q[1]
			break
		for d in range(4):
			nr = q[0] + dr[d]
			nc = q[1] + dc[d]
			if 0 <= nr < N and 0 <= nc < N and visit[nr][nc] == 0 and nav[nr][nc] != 1:
				que.append((nr, nc))
				visit[nr][nc] = visit[q[0]][q[1]] + 1
	else:
		print(-1)
		break
	if costa+costb > gas:
		print(-1)
		break
	else:
		gas = gas - costa + costb
else:
	print(gas)

'''
6 3 13
0 0 1 0 0 0
0 0 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 1 0
0 0 0 1 0 0
6 5
2 2 5 6
5 4 1 6
4 2 3 5
'''