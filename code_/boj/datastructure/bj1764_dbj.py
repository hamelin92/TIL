import sys

N, M = map(int, sys.stdin.readline().split())
dj = {sys.stdin.readline().strip("\n") for _ in range(N)}
bj = {sys.stdin.readline().strip("\n") for _ in range(M)}
ans = sorted(dj&bj)
print(len(ans))
print(*ans, sep="\n")