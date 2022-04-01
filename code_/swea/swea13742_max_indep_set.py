#from collections import defaultdict
T = int(input())
for tc in range(1, T+1):
	N, M = map(int,input().split()) # 1 <= N <= 100 , N-1 <= M <= N + 15
	edges = [tuple(map(int,input().split())) for _ in range(M)]
	graph = [[0]*(N+1) for _ in range(N+1)]
	for edge in edges:
		graph[edge[0]][edge[1]] = 1
		graph[edge[1]][edge[0]] = 1
	#ordered = sorted(graph, key = lambda x: len(graph[x]), reverse=True)
	# print(graph)
	#print(ordered)
	V_C = set()
	selection = 0
	s = [0]*(N+1)
	chk = 0
	while len(V_C) == selection:
		chk = 0
		for i in range(1,N+1):
			if sum(graph[i]) > 0:
				break
		else:
			break
		for i in range(1,N+1):
			for j in range(1,N+1):
				if graph[i][j]:
					s[i] += sum(graph[j])
		max_s = max(s)
		k = 1
		for i in range(1,N+1):
			if max_s < s[i]:
				t = i
			elif max_s == s[i] and sum(graph[i-k]) <= sum(graph[i]):
				t = i
			elif max_s == s[i] and sum(graph[i-k]) > sum(graph[i]):
				t = i-k
				k = k+1
		V_C |= {t}
		selection += 1
		for i in range(1,N+1):
			graph[i][t] = 0
			graph[t][i] = 0
	ans = N-len(V_C) if len(V_C) < N else 1
	print(f'#{tc} {ans}')


'''

3
2 1
1 2
5 5
1 2
2 3
3 4
4 5
5 1
4 5
1 2
2 3
3 4
4 1
1 3
'''