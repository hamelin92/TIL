import math
T = int(input())
for tc in range(1, T+1):
	a, d, n = map(int, input().split())
	m = 1000003
	if n >= m and d > 0:
		answer = 0
	elif a == 0 and d == 0:
		answer = 0
	elif a == 1 and d == 0:
		answer = 1
	elif d == 0:
		answer = (a ** n)%m
	else:
		g = math.gcd(m-a,d)
		q = (m-a)//g
		if q < n:
			answer = 0
		else:
			prod = 1
			for i in range(n//2):
				prod *= (a+i*d)*(a+(n-1-i)*d)
				if prod > m:
					prod %= m
			if n%2:
				prod =prod * (a + (n//2)*d)
			answer = prod%m
	print(answer)