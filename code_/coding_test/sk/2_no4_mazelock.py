def solution(n, m, k, records):
	answer = []
	key = [[1] for _ in range(k)]
	cnt = [-1]*(n+1)
	skip = [1]*k
	for i in range(k):
		if cnt[records[0][i]] == -1:
			cnt[records[0][i]] = i
		else:
			key[i] = key[cnt[records[0][i]]]
			skip[i] = 0
	gap_limit = [m-1]*(k)
	for record in records:
		for i in range(k):
			if skip[i]:
				if i == 0:
					if abs(gap_limit[i]) > abs(record[i]):
						gap_limit[i] = record[i]
					key[i][0] = gap_limit[i]
				else:
					if abs(gap_limit[i]) > abs(record[i] - record[i-1]):
						gap_limit[i] = record[i] - record[i-1]
					key[i][0] = key[i-1][0]+gap_limit[i]
	answer = key
	return answer

print(solution(8, 4, 4, [[1, 6, 1,5]]))

# N개의 배열 중 임의의 m개의 칸에 1~m의 숫자가 크기 순서대로 들어잇다.
# m 이하의 k 자리인 비밀번호가 있고 records는 비밀번호를 누른 배열의 칸을 기록한 것들이다.
# 비밀번호를 누를때마다 배열 안에 숫자의 위치는 무작위로 결정되므로 누르는 칸의 번호는 매번 달라질 수 있다.
# records를 바탕으로 가능한 비밀번호 중 사전순으로 가장 마지막인 값을 반환하는 함수를 만들어라.
