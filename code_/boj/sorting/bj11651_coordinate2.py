import sys

N = int(sys.stdin.readline())
pts = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
pts.sort(key=lambda x: (100001 + x[1])*200001 + x[0])
for pt in pts:
    print(*pt)