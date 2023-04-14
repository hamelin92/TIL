def primes(n):
    b = [True] * (n + 1)
    ps = []
    for p in range(2, n + 1):
        if b[p]:
            ps.append(p)
            b[p::p] = [False for _ in range(p, n + 1, p)]
    return ps

N = int(input())
pl = primes(N)
spl = [0] + pl[:]
lth = len(spl)
for i in range(1, lth):
    spl[i] += spl[i-1]
ans = 0
start = end = 0
while True:
    psum = spl[end] - spl[start]
    if psum < N:
        if end >= lth-1:
            break
        end += 1
    elif psum == N:
        ans += 1
        if end >= lth-1:
            break
        end += 1
    else:
        start += 1
print(ans)
