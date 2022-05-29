from itertools import permutations

N = int(input())
A = list(map(int, input().split()))
operations = list(map(int, input().split())) # [+, -, *, /]
opers = []
for d in range(4):
	opers += [d]*operations[d]

max_v = -1000000001
min_v = 1000000001
for p in set(permutations(opers, len(opers))):
	result = A[0]
	for n in range(N-1):
		if p[n] == 0:
			result += A[n+1]
		elif p[n] == 1:
			result -= A[n+1]
		elif p[n] == 2:
			result *= A[n+1]
		else:
			num = 1
			if result < 0:
				num = -1
			result = num*int(abs(result)/A[n+1])
	if result > max_v:
		max_v = result
	if result < min_v:
		min_v = result
print(max_v)
print(min_v)
