def solution(numbers, hand):
	answer = ''
	left = [3,0]
	right = [3,2]
	keypad = {1: (0,0),2: (0,1),3: (0,2),4: (1,0),5: (1,1),6: (1,2),7: (2,0),8: (2,1),9: (2,2),0: (3,1)}
	for n in numbers:
		if n in {1,4,7}:
			answer += 'L'
			left = keypad[n]
		elif n in {3,6,9}:
			answer += 'R'
			right = keypad[n]
		else:
			left_d = abs(keypad[n][0] - left[0])+ abs(keypad[n][1] - left[1])
			right_d = abs(keypad[n][0] - right[0]) + abs(keypad[n][1] - right[1])
			if left_d < right_d:
				answer += 'L'
				left = keypad[n]
			elif left_d > right_d:
				answer += 'R'
				right = keypad[n]
			else:
				if hand == 'right':
					answer += 'R'
					right = keypad[n]
				else:
					answer += 'L'
					left = keypad[n]
	return answer