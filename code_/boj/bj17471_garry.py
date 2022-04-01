from collections import defaultdict
N = int(input())
population = list(map(int, input().split()))
region_info = [list(map(int, input().split())) for _ in range(N)]
graph = defaultdict(list)
