from collections import deque
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
arr = [list(map(int, input().split())) for _ in range(6)]
s = (1,0)
visit = [[0]*4 for _ in range(6)]
que = deque()
que.append(s)
visit[s[0]][s[1]] = 1
while que:
	v = que.popleft()
	if arr[v[0]][v[1]] == 2:
		ans = v
		break
	for d in range(4):
		ni = v[0] + di[d]
		nj = v[1] + dj[d]
		if 0 <= ni < 6 and 0 <= nj < 4 and visit[ni][nj] == 0 and arr[ni][nj] != 1:
			visit[ni][nj] += visit[v[0]][v[1]] + 1
			que.append((ni,nj))
print(visit[ans[0]][ans[1]]-1)


'''
0 1 0 0
3 1 2 2
0 1 0 2
0 1 0 2
0 0 0 0
0 0 0 0
'''