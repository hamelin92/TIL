from collections import defaultdict


def dfs(q, n):
	if n == 4: # n이 0부터 증가해서 4가 된 순간 5명의 관계 ABCDE의 존재가 확인된다.
		answers[0] = 1
		return
	for r in relation[q]:
		if visit[r] == 0:
			visit[r] = 1
			dfs(r,n+1)
			visit[r] = 0
	else:
		return


N, M = map(int, input().split())
relation = defaultdict(list)
visit = [0]*N
answers = [0]
for rel in range(M): # 친구 관계 그래프 나타내기
	u, v = map(int, input().split())
	relation[u].append(v)
	relation[v].append(u)
for s in range(N): # 0부터 N-1까지 각각을 시작점으로 dfs 실행.
	visit[s] = 1
	dfs(s, 0)
	visit[s] = 0
	if answers[0] == 1: # 관계 ABCDE가 존재하면 1을 출력하고 종료
		print(1)
		break
else: # for문이 끝날 때까지 break가 없다면 0을 출력
	print(0)
