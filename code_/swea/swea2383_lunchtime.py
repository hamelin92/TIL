
T = int(input())
for tc in range(1, T+1):
	N = int(input())
	room = [list(map(int, input().split())) for _ in range(N)]
	people = []
	stair = []
	for i in range(N):
		for j in range(N):
			if room[i][j] == 1:
				people.append((i,j))
			elif room[i][j] > 1:
				stair.append((i,j,room[i][j]))
	distance = []
	for p in people:
		p_info = []
		for s in stair:
			dis = abs(p[0]-s[0]) + abs(p[1]-s[1]) + s[2] + 1
			p_info.append(dis)
		distance.append(p_info)
	que = []
	cnt = [0,0]
	for i in range(len(distance)):
		dis = distance[i]
		if dis[0] < dis[1]:
			que.append([dis[0], i])
			cnt[0] += 1
		else:
			que.append([dis[1], i])
			cnt[1] += 1
	que.sort()
	result = []
	for q in que: # 사람들을 줄 세우기 ( 그리디하게 각각 가장 빠르게 가는 방법(타인 고려 X)으로 정렬 )
		if cnt[0] > 3:
			q[0] = min(q[0] + stair[0][2], distance[q[1]][1]) # 계단1이 차있는 경우 자리가 생길떄까지 대기 vs 다른 쪽 계단을 가는 경우랑 비교
			cnt[0] -= 1
		if cnt[1] > 3:
			q[0] = min(q[0] + stair[1][2], distance[q[1]][0])
			cnt[1] -= 1
		result.append(q[0])
	print(f'#{tc} {max(result)}')