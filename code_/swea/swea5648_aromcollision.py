T = int(input())
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]
x + dx[k] * t, y + dy[k] * t
plane = [[0]*2001 for _ in range(2001)]
for tc in range(1, T+1):
	N = int(input())
	dynamics = [[], [], [], []]
	for i in range(N):
		x, y, direction, energy = map(int, input().split())
		dynamics[direction].append([x, y, energy])
