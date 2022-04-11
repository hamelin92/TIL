from pprint import pprint


def solution(info, query):
	def check(arr2):
		global k
		if case[i] == '-':
			return True
		elif case[i][0] != arr2[i][0]:
			return False
		else:
			return True
	def minimal(n):
		if idx_dic.get(n) is not None:
			return idx_dic.get(n)
		N = len(info)
		left = 0
		right = N-1
		if n > int(info[right][4]):
			return N
		elif n < int(info[left][4]):
			return 0
		while left < right:
			mid = (left+right)//2
			if mid+1 < N and int(info[mid][4]) < n <= int(info[mid+1][4]):
				idx_dic[n] = mid+1
				return mid+1
			elif int(info[mid][4]) < n:
				left = mid+1
			else:
				right = mid

	answer = []
	info = [p.split() for p in info]
	info.sort(key=lambda x: int(x[4]))
	N = len(info)
	idx_dic = dict()
	query = [list(filter(lambda x: x[0] != 'a', q.split())) for q in query]
	for case in query:
		n = minimal(int(case[-1]))
		tmp_list = info[n:]
		for i in range(4):
			k = i
			tmp_list = list(filter(check, tmp_list))
		result = len(tmp_list)
		answer.append(result)
	print(answer)
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