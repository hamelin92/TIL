def primes(m, n):
    b = [True] * (n + 1)
    ps = []
    for p in range(2, n + 1):
        if b[p]:
            if p >= m:
                ps.append(p)
            b[p::p] = [False for _ in range(p, n + 1, p)]
    return ps


M, N = map(int, input().split())
for p in primes(M, N):
    print(p)
