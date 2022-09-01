T = int(input())
for tc in range(T):
	p = input()
	n = int(input())
	x = input()
	x_parsed = list(map(int, filter(lambda str: bool(str), x[1:-1].split(','))))
	sign = 1
	left = 0
	right = n
	for func in p:
		if func == 'R':
			sign *= -1
		else:
			if sign == 1:
				left += 1
			else:
				right -= 1
	if right <= left:
		print('error')
	else:
		if sign == 1:
			result = x_parsed[left:right]
		else:
			if left == 0:
				result = x_parsed[right-1::-1]
			else:
				result = x_parsed[right-1: left-1:-1]
		answer = str(result).replace(' ','')
		print(answer)