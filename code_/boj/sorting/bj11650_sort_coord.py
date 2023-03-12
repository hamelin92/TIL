import sys

N = int(sys.stdin.readline())
pts = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
pts.sort(key=lambda x: (x[0], x[1]))
for p in pts:
    print(*p)