from pprint import pprint
from collections import deque
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
T = int(input())
for tc in range(1, T+1):
	N,M = map(int,input().split())
	garden = [list(map(int, input().split())) for _ in range(N)]
	s = list(map(int,input().split()))
	used = [[0]*M for _ in range(N)]
	que = deque()
	que.append(s)
	used[s[0]][s[1]] = garden[s[0]][s[1]]
	live = [0]*(N*M+1)
	day = 1
	while que:
		cnt = len(que)
		for k in range(cnt):
			q = que.popleft()
			live[day] += 1
			if garden[q[0]][q[1]]+day < N*M:
				live[garden[q[0]][q[1]]+day] -= 1
			for d in range(4):
				nr = q[0] + dr[d]
				nc = q[1] + dc[d]
				if 0 <= nr < N and 0 <= nc < M and used[nr][nc] == 0 and garden[nr][nc] > 0:
					que.append([nr, nc])
					used[nr][nc] = 1
		day += 1
	max_flower = live[0]
	max_day = 0
	for i in range(1,N*M//2):
		live[i] += live[i-1]
		if live[i] > max_flower:
			max_flower = live[i]
			max_day = i
	print(f'#{tc} {max_day}일 {max_flower}개')