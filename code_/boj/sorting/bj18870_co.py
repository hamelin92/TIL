import sys

N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))
res = [0]*N
X_s = sorted(enumerate(X), key=lambda x: x[1])
last = X_s[0][1]
cnt = 0
for k in range(N):
    if X_s[k][1] > last:
        last = X_s[k][1]
        cnt += 1
    res[X_s[k][0]] = cnt
print(*res)