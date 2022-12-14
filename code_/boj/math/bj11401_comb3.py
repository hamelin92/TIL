def modulo_inverse(a, b):
    s0, s1 = 0, 1
    if a > b:
        s0, s1 = 1, 0
    while a > 1 and b > 1:
        d = b//a
        s0, s1 = s1, s0 - d * s1
        a, b = b - d*a, a
    return s1

N, K = map(int, input().split())
k = min(N-K, K)
N_fact = 1
K_fact = 1
for i in range(k):
    N_fact *= (N-i)
    K_fact *= (k-i)
    N_fact %= 1000000007
    K_fact %= 1000000007
inverse = modulo_inverse(K_fact, 1000000007)
if inverse < 0:
    inverse += 1000000007
ans = (N_fact * inverse) % 1000000007
print(ans)