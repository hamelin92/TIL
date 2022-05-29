def solution(n, t, m, p):
	from math import log
	answer = ''
	length = m * (t-1) + p
	for i in range(t):
		k = p + m*i -1
		digits = int(log(k,n)) if k > 0 else 0
		res = k%(digits * n**(digits-1) if digits > 0 else n)
		tres = res//(digits if digits > 0 else 1)
		num = n ** digits + tres
		print(k)
		print(res)
	return answer
solution(16,16,2,2)

'''
1*10 + 2 *90 + 3*900 + 4 * 9000
16	16	2	2
(n-1)*n**d-1
'''