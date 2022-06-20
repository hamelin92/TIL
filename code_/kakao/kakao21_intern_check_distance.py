def solution(places):
	from itertools import combinations
	answer = []
	checks = []
	for i in range(5):
		check = []
		for j in range(5):
			for k in range(5):
				if places[i][j][k] == 'P':
					check.append((j,k))
		checks.append(check)
	for i in range(5):
		flag = 0
		place = places[i]
		check = checks[i]
		for chks in combinations(check, 2):
			md = abs(chks[0][0] - chks[1][0]) + abs(chks[0][1] - chks[1][1])
			if md < 2:
				break
			elif md == 2:
				if chks[0][0] == chks[1][0] and place[chks[0][0]][(chks[0][1]+chks[1][1])//2] == 'O':
					break
				if chks[0][1] == chks[1][1] and place[(chks[0][1] + chks[1][1]) // 2][chks[0][0]] == 'O':
					break
				if place[chks[0][0]][chks[1][1]] == 'O' or place[chks[1][0]][chks[0][1]] == 'O':
					break
		else:
			flag = 1
			answer.append(1)
		if flag==0:
			answer.append(0)
	return answer
solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])
'''
[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
'''