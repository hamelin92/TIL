import sys


N, M, B = map(int, sys.stdin.readline().split())
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ground_h = [0] * 257
min_h = 256
max_h = 0
for i in range(N):
    for j in range(M):
        ground_h[ground[i][j]] += 1
        if ground[i][j] < min_h:
            min_h = ground[i][j]
        elif ground[i][j] > max_h:
            max_h = ground[i][j]
results = []
for k in range(min_h, max_h+1):
    t = 0
    blocks = 0
    for g in range(min_h, k):
        blocks += (k-g)*ground_h[g]
        t += (k-g)*ground_h[g]
    for g in range(k+1, max_h+1):
        t += ground_h[g]*(g-k)*2
        blocks -= ground_h[g]*(g-k)
    if blocks > B:
        continue
    results.append([t, k])
ans = max(results, key=lambda x: -x[0] * 256 + x[1])
print(ans[0], ans[1])
