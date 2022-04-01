from collections import deque
N, K = map(int,input().split())
visit = [[0]*N for _ in range(N)]
cnt = [[] for _ in range(K+1)]
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
test_tube = [list(map(int, input().split())) for _ in range(N)]
que = deque([])
for i in range(N):
	for j in range(N):
		if test_tube[i][j] > 0:
			cnt[test_tube[i][j]].append((i,j))
			visit[i][j] = 1
for k in range(1,K+1):
	que.extend(cnt[k])
cnt = 0
S, X, Y = map(int, input().split())
while que:
	v = que.popleft()
	if visit[X-1][Y-1] != 0:
		ans = test_tube[X-1][Y-1]
		break
	if visit[v[0]][v[1]] == S+1:
		ans = test_tube[X-1][Y-1]
		break
	for d in range(4):
		ni = v[0] + di[d]
		nj = v[1] + dj[d]
		if 0 <= ni < N and 0 <= nj < N and visit[ni][nj] == 0:
			que.append((ni,nj))
			test_tube[ni][nj] = test_tube[v[0]][v[1]]
			visit[ni][nj] = visit[v[0]][v[1]] + 1
else:
	ans = test_tube[X - 1][Y - 1]

print(ans)

'''
3 3
1 1 2
1 1 1
3 1 1
2 3 2

예제 입력 2 

7 7
1 0 2 0 0 0 3
0 7 0 0 0 0 0
3 0 6 0 0 0 0
1 2 0 0 0 5 0
0 0 0 0 0 4 0
0 0 0 0 0 0 1
0 0 0 0 0 0 1
5 7 2
'''
