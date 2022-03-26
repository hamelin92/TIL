N, K = map(int, input().split())
seq = list(map(int, input().split()))
max_sum = partial_sum = sum(seq[0:K]) # 0~K-1까지 합

for i in range(N-K):
	partial_sum += seq[K+i]-seq[i] # K+i번쨰를 더하고 i번째를 빼준다.
	if partial_sum > max_sum: # 최대값 갱신하면 교체해ㅈㄱ주
		max_sum = partial_sum
print(max_sum)