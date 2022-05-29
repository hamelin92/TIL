def solution(m, musicinfos):
	def melody_list(string):
		result = []
		for s in string:
			if s == '#':
				result[-1] += s
			else:
				result.append(s)
		return result
	results = []
	new_m = melody_list(m)
	length = len(new_m)
	musicinfos = [info.split(',') for info in musicinfos]
	for info in musicinfos:
		minutes = 60*(int(info[1][:2]) - int(info[0][:2])) + int(info[1][3:]) - int(info[0][3:])
		if minutes < length:
			continue
		else:
			melody = melody_list(info[3])
			k = 0
			for i in range(minutes):
				if melody[i%len(melody)] == new_m[k]:
					k += 1
				else:
					k = 0
					if melody[i%len(melody)] == new_m[k]:
						k += 1
				if k == length:
					results.append([info[2], minutes])
					break
	if results:
		max_ans = 0
		for i in range(len(results)):
			if results[i][1] > results[max_ans][1]:
				max_ans = i
		answer = results[max_ans][0]
	else:
		answer = '(None)'
	return answer
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
'''
"ABCDEF#G", ["12:00,12:14,HELLO,CDEF#GAB", "13:00,13:05,WORLD,ABCDEF#"]
'''