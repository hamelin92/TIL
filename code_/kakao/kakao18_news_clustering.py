def solution(str1, str2):
	from collections import defaultdict
	str1 = str1.casefold()
	str2 = str2.casefold()
	dic1 = defaultdict(int)
	dic2 = defaultdict(int)
	dic_u = defaultdict(int)
	for i in range(len(str1)-1):
		for s in str1[i:i+2]:
			if not s.islower():
				break
		else:
			dic1[str1[i:i+2]] += 1
			dic_u[str1[i:i+2]] += 1
	for i in range(len(str2)-1):
		for s in str2[i:i+2]:
			if not s.islower():
				break
		else:
			dic2[str2[i:i+2]] += 1
			dic_u[str2[i:i + 2]] += 1
	intersection = 0
	union = 0
	for key in dic_u.keys():
		if dic1.get(key) and dic2.get(key):
			intersection += min(dic1[key], dic2[key])
			union += max(dic1[key], dic2[key])
		else:
			union += dic_u[key]
	if union > 0:
		answer = int(65536 * ( intersection / union ))
	else:
		answer = 65536
	return answer

print(solution('FRANCE', 'french'))