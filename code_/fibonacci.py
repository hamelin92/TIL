memo = [1,1]
def fibonacci(n):
	if n <= len(memo)-1:
		return memo[n-1]
	elif n == len(memo):
		m = memo[-1]+memo[-2]
		memo.append(m)
		return m
	else:
		return fibonacci(n-1) + fibonacci(n-2)
def fibonacci2(n):
	F = [1,1]
	for i in range(2,n):
		F.append(F[i-1] + F[i-2])
	return F[n-1]
print(fibonacci2(10))