def modulo_inverse(a, b):
    s0, s1 = 0, 1
    if a > b:
        s0, s1 = 1, 0
    while a > 1 and b > 1:
        d = b//a
        s0, s1 = s1, s0 - d * s1
        a, b = b - d*a, a
    return s1


def exp_mod(A, B, C):
    A = D = A%C
    seq = []
    while B > 1:
        seq.append(B%2)
        B = B//2
    for exp in seq[::-1]:
        if exp:
            A = (A ** 2) * D
        else:
            A = (A ** 2)
        A = A%C
    return A


def product(a: int, b: int):
    m = 500000004
    even_sign = (b+1)%2
    # product of numbers where numbers are from a to b
    even_product = 2 ** (b//2-(a+1)//2+1) * product((a+1)//2, b//2)
    # k = a//2 to k = b//2-odd_sign product of (2k+1)
    start = a//2
    end = b//2 - even_sign
    odd_product = 2 ** (end-start+1) * product(start+m, end+m)
    return even_product*odd_product*1000000007




N, K = map(int, input().split())
k = min(N-K, K)
N_fact = 1
K_fact = 1
for i in range(k):
    N_fact *= (N-i)
    K_fact *= (k-i)
    N_fact %= 1000000007
    K_fact %= 1000000007
inverse = modulo_inverse(K_fact, 1000000007) % 1000000007
ans = (N_fact * inverse) % 1000000007
print(ans)