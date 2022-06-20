from itertools import combinations

T = int(input())
for tc in range(T):
	N = int(input())
	vectors = [list(map(int, input().split())) for _ in range(N)]
	x_sum = y_sum = 0
	for v in vectors:
		x_sum += v[0]
		y_sum += v[1]
	min_vector = 4000000
	for cb in combinations(range(N), N//2):
		x_s, y_s = x_sum, y_sum
		for n in cb:
			x_s -= 2 * vectors[n][0]
			y_s -= 2 * vectors[n][1]
		dist = (x_s**2 + y_s**2)**(1/2)
		if dist < min_vector:
			min_vector = dist
	print(min_vector)

