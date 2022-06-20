def probablity(p,lev):
	global max_result, N
	if p <= max_result:
		return
	if lev == N:
		if p > max_result:
			max_result = p
	else:
		for j in range(N):
			if arr[j] == 0:
				arr[j] = 1
				probablity(p*probs[lev][j]/100, lev+1)
				arr[j] = 0

T = int(input())
for tc in range(1, T+1):
	N = int(input())
	probs= [list(map(int, input().split())) for _ in range(N)]
	arr = [0]*N
	max_result = 0
	probablity(1, 0)

	print(f'#{tc}{round(max_result*100,6) : .6f}')