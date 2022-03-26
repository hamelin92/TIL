T = int(input())
for tc in range(1, T+1):
	N =int(input())
	info = [list(map(int, input().split())) for _ in range(N)]
	cnt = [0]*1001
	for bus in info:
		cnt[bus[1]] += 1
		cnt[bus[2]] += 1
		if bus[0] == 1:
			for i in range(bus[1]+1, bus[2]):
				cnt[i] += 1
		elif bus[0] == 2:
			for i in range(bus[1]+2, bus[2], 2):
				cnt[i] += 1
		else:
			if bus[1]%2 == 0:
				a = (bus[1]//4)*4+4
				for i in range(a, bus[2], 4):
					cnt[i] += 1
			else:
				a = (bus[1]//3)*3+3
				for i in range(a, bus[2], 3):
					if i%10 != 0:
						cnt[i] += 1

	print(f'#{tc} {max(cnt)}')