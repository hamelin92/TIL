def solution(s):
	result = ''
	num_dic = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
	tmp = ''
	for w in s:
		if w.isnumeric():
			result += w
		else:
			tmp += w
			if num_dic.get(tmp) != None:
				result += num_dic.get(tmp)
				tmp =''
	answer = int(result)
	return answer
