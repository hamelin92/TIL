T = int(input())
for tc in range(1, T+1):
	K = int(input())
	gears = [list(map(int, input().split())) for _ in range(4)]
	rotation = [list(map(int, input().split())) for _ in range(K)]
	score = 0
	state = [0] *4
	for r in rotation:
		orient = [0] * 4
		num = r[0] -1
		drc = r[1]
		orient[num] = -drc
		for i in range(1,4):
			ni = num-i
			if ni >= 0:
				if gears[ni][(state[ni]+2)%8] != gears[ni+1][(state[ni+1]+6)%8]:
					orient[ni] = -orient[ni+1]
				else:
					break
			else:
				break
		for i in range(1,4):
			ni = num+i
			if ni < 4:
				if gears[ni-1][(state[ni-1]+2)%8] != gears[ni][(state[ni]+6)%8]:
					orient[ni] = -orient[ni-1]
				else:
					break
			else:
				break

		for i in range(4):
			state[i] += 8+orient[i]
			state[i] %= 8
	for i in range(4):
		score += gears[i][state[i]] * 2**i
	print(f'#{tc} {score}')