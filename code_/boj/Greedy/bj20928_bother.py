N, M = map(int, input().split()) # N개의 지점, 목적지 M ( 1 <= N <= 100000, 1 <= M <= 1000000
p = list(map(int, input().split())) # N개의 지점 좌표
x = list(map(int, input().split())) # N개의 지점별 인력거꾼의 이동거리

cnt = 0
first = min(M, p[0]+x[0])
dp = [0]*first + [-1]*(M+1-first)


for i in range(1, N):
	next = min(p[i]+x[i], M)
	if p[i] <= first and next > first:
		for j in range(first, next):
			dp[j] = dp[p[i]] + 1
		first = next
print(dp[M-1])



# def count_func(start, change):
# 	idx = sel = start
# 	cnt = change
#
# 	for p_idx in range(start, N):
# 		if p[p_idx] <= p[idx] + x[idx]:
# 			if p[p_idx] + x[p_idx] >= p[sel] + x[sel]:
# 				sel = p_idx
# 				if p[sel] + x[sel] >= M:
# 					cnt += 1
# 					return cnt
# 		elif p[sel] + x[sel] >= p[p_idx] > p[idx] + x[idx]:
# 			cnt += 1
# 			idx = sel
# 			sel = sel if p[p_idx] + x[p_idx] < p[sel] + x[sel] else p_idx
# 			if p[idx] + x[idx] >= M:
# 				return cnt
# 		else:
# 			if p[idx] + x[idx] < M:
# 				return -1
# 	else:
# 		if p[idx] + x[idx] < M:
# 			return -1
# 		else:
# 			return cnt
