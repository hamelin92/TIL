from math import gcd
N = int(input())
D = [1] * (N+1)
for i in range(2,N+1):
    D[i] = D[i-1] + D[i-2]
answer = 0
cong = 1000000007
for i in range(1, N+1):
    answer += D[gcd(i+1, N+1)-1]
    answer %= cong
print(answer)
# factors = []
# N_fact = N
# for j in range(2, int(N ** (1/2))+1):
#     if N_fact%j == 0:
#         factor = [j, 0]
#         while N_fact%j == 0:
#             N_fact = N_fact//j
#             factor[1] += 1
#         factors.append(factor)
# else:
#     if N_fact > 1:
#         factors.append([N_fact, 1])
# for fact in factors:
#     for level in range(1, fact[1]+1):
#         cnt = N//fact[0]