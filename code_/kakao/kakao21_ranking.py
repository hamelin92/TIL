from pprint import pprint


def solution(info, query):
	from collections import defaultdict
	from re import sub
	def trans(arr):
		arr[-1] = int(arr[-1])
		return arr

	def check(arr2):
		for j in range(4):
			if case[j] == '-':
				continue
			if case[j][0] != arr2[j][0]:
				return False
		else:
			return True
	def minimal(n,key):
		N = len(info_dic[key])
		left = 0
		right = N-1
		if n > info_dic[key][right]:
			return N
		elif n <= info_dic[key][left]:
			return 0
		while left < right:
			mid = (left+right)//2
			if mid+1 < N and info_dic[key][mid] < n <= info_dic[key][mid+1]:
				return mid+1
			elif info_dic[key][mid] < n:
				left = mid+1
			else:
				right = mid
	answer = []

	info = [trans(p.split()) for p in info]
	print(info)
	info.sort(key=lambda x: x[4])
	info_dic = defaultdict(list)
	for i in info:
		info_dic[(i[0], i[1], i[2], i[3])].append(i[4])
	query = [sub('and','', q).split() for q in query]
	for case in query:
		fkeys = list(filter(check, info_dic.keys()))
		result = 0
		for key in fkeys:
			n = minimal(int(case[-1]),key)
			result += len(info_dic[key]) - n
		answer.append(result)
	return answer


solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])



'''
["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
[1,1,1,1,2,4]
언어	직군	경력	소울 푸드	점수
java	backend	junior	pizza	150
python	frontend	senior	chicken	210
python	frontend	senior	chicken	150
cpp	backend	senior	pizza	260
java	backend	junior	chicken	80
python	backend	senior	chicken	50
'''