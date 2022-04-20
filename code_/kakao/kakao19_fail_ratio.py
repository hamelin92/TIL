def solution(N, stages):
	results = []
	cnt = [0]*(N+1)
	total = len(stages)
	for i in stages:
		cnt[i-1] += 1
	for i in range(N):
		if total > 0 and cnt[i] > 0:
			results.append([cnt[i]/total,i+1])
			total -= cnt[i]
		else:
			results.append([0,i+1])

	results.sort(key=lambda x: x[0], reverse=True)
	answer = [x[1] for x in results]

	return answer

solution(4, [4,4,4,4,4])