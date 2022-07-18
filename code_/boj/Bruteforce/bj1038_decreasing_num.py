from math import comb


def combination(arr, r):

	def generate(chosen):
		global N_cop, result
		if len(chosen) == r:
			N_cop += 1
			if N_cop == comb(10, r)+1:
				result = chosen[:]
			return

		start = arr.index(chosen[-1]) + 1 if chosen else 0
		for nxt in range(start, len(arr)):
			chosen.append(arr[nxt])
			generate(chosen)
			chosen.pop()
	generate([])


N = int(input())
if N > 2**10 - 2:
	print(-1)
else:
	N_cop = N + 1
	n = 1
	while N_cop > comb(10,n):
		N_cop -= comb(10,n)
		n += 1
	result = []
	combination(list(range(9,-1,-1)), n)
	answer = 0
	for i in range(n):
		answer += result[n-i-1] * 10**i
	print(answer)
