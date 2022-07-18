from math import gcd

N = int(input())
m = [int(input()) for _ in range(N)]
m_res = [m[k+1]-m[0] for k in range(N-1)]
M = m_res[0]
for num in m_res:
	M = gcd(M, num)
answer = []
for fac in range(2,int(M**(1/2))+1):
	if M % fac == 0:
		answer.append(fac)
		if fac != M//fac:
			answer.append(M//fac)
else:
	answer.append(M)
answer.sort()
print(*answer)
