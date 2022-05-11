def bc_chk(i,j):
	global A
	ans = []
	for k in range(A):
		if abs(j - ap[k][0]) + abs(i - ap[k][1]) <= ap[k][2]:
			ans.append([k, ap[k][3]])
	ans.sort(key=lambda x: x[1], reverse=True)
	return ans

def values(a,b):
	a_in = bc_chk(a[0], a[1])
	b_in = bc_chk(b[0], b[1])
	tmp = []
	if a_in and b_in and a_in[0][0] == b_in[0][0]:
		tmp.append(a_in[0][1])
		if len(a_in) > 1:
			tmp.append(a_in[1][1] + b_in[0][1])
		if len(b_in) > 1:
			tmp.append(b_in[1][1] + a_in[0][1])
	else:
		tmp_val = 0
		if a_in:
			tmp_val += a_in[0][1]
		if b_in:
			tmp_val += b_in[0][1]
		tmp.append(tmp_val)
	return max(tmp)

di = [0, -1, 0, 1, 0]
dj = [0, 0, 1, 0, -1]

T = int(input())
for tc in range(1, T+1):
	M, A = map(int,input().split())
	user_a = list(map(int, input().split()))
	user_b = list(map(int, input().split()))
	ap = [list(map(int, input().split())) for _ in range(A)]
	co_a = [1, 1]
	co_b = [10, 10]
	answer = 0
	answer += values(co_a,co_b)
	for m in range(M):
		co_a[0] += di[user_a[m]]
		co_a[1] += dj[user_a[m]]
		co_b[0] += di[user_b[m]]
		co_b[1] += dj[user_b[m]]
		answer += values(co_a,co_b)
	print(f'#{tc} {answer}')