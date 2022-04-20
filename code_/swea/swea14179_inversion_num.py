T = int(input())
modulo = 1000000007
for tc in range(1, T+1):
	N, K = map(int, input().split())
	A = list(enumerate(map(int, input().split())))
	A.sort(key=lambda x: x[1])
	ans = 0
	for i in range(1, N):
		cnt = 0
		cnt_all = 0
		for j in range(i):
			if A[i][1] > A[j][1]:
				cnt_all += 1
				if A[i][0] < A[j][0]:
					cnt += 1
		res_i = (K*(2*cnt + (K-1)*cnt_all)//2)%modulo
		ans += res_i
		ans %= modulo
	print(f'#{tc} {ans}')