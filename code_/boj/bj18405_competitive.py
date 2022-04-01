from collections import defaultdict
N, K = map(int,input().split())
test_tube = defaultdict(list)
visit = [[0]*N for _ in range(N)]
cnt = [0]*(K+1)
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
for i in range(N):
	tube = list(map(int, input().split()))
	for j in range(N):
		test_tube[tube[j]].append((i,j))
		if tube[j] > 0:
			visit[i][j] = 1
S, X, Y = map(int, input().split())
ans = 0
for s in range(S):
	if ans > 0:
		break
	for k in range(1,K+1):
		if ans > 0:
			break
		t = len(test_tube[k])
		for j in range(cnt[k], t):
			if test_tube[k][j][0] == X-1 and test_tube[k][j][1] == Y-1:
				ans = k
				break
			if ans > 0:
				break
			for d in range(4):
				ni = test_tube[k][j][0] + di[d]
				nj = test_tube[k][j][1] + dj[d]
				if 0 <= ni < N and 0 <= nj < N and visit[ni][nj] == 0:
					if ni == X-1 and nj == Y-1:
						ans = k
						break
					cnt[k] += 1
					visit[ni][nj] = 1
					test_tube[k].append((ni,nj))
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
