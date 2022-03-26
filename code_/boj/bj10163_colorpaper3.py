N = int(input())
papers = [list(map(int, input().split())) for _ in range(N)]
grid = [[0]*1001 for _ in range(1001)]
areas = [0]*N
# 정확하고 빠른 해법 필요