def solution(dartResult):
	scores = [0]
	tmp = ''
	for score in dartResult:
		if score.isnumeric():
			tmp += score
		else:
			if score in ['S', 'D', 'T']:
				now = int(tmp)
				tmp = ''
				if score == 'D':
					now **= 2
				elif score == 'T':
					now **= 3
				scores.append(now)

			if score == '*':
				scores[-1] *= 2
				scores[-2] *= 2
			elif score == '#':
				scores[-1] *= -1
	answer = sum(scores)
	return answer

print(solution('1S2D*3T'))