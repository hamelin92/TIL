def modulo_inverse(a, b):
    s0, s1 = 0, 1
    if a > b:
        s0, s1 = 1, 0
    while a > 1 and b > 1:
        d = b//a
        s0, s1 = s1, s0 - d * s1
        a, b = b - d*a, a
    return s1


def powers(A,B):
    global modulo
    A = D = A%modulo
    seq = []
    while B > 1:
        seq.append(B%2)
        B = B//2

    for exp in seq[::-1]:
        if exp:
            A = (A ** 2) * D
        else:
            A = (A ** 2)
        A = A%modulo
    return A if B > 0 else 1


def factoriaztion(n):
    factors = []
    for j in range(2, int(n ** (1/2))+1):
        if n%j == 0:
            factor = [j, 0]
            while n%j == 0:
                n = n//j
                factor[1] += 1
            factors.append(factor)
    else:
        if n > 1:
            factors.append([n, 1])
    return factors


def factorial(n):
    factors = factoriaztion(n)
    for factor in factors:
        factor[0]



factorials = [1]*4000001
computed = 1
modulo = 1000000007
M = int(input())
for i in range(M):
    N, K = map(int, input().split())
    if N > computed:
        for n in range(computed+1, N+1):
            factorials[n] = factorials[n-1]*n%modulo
        computed = N
    divider = factorials[K] * factorials[N-K] % modulo
    div = powers(divider, modulo-2)
    print(factorials[N]*div%modulo)
    
