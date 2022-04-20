import math
n = int(input())
K = int(math.sqrt(n))
B = int(math.sqrt(K))
s = 0
b = 0
while 1:
	a = b
	b = min(b + B, K)

	for k in range(a+1, b+1):
		s = s + mu[k] * n//(k*k)

