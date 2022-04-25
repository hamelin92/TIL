def solution(record):
	in_out = {'Enter': '들어왔습니다.', 'Leave': '나갔습니다.'}
	record = [r.split() for r in record]
	result = []
	rec_dic = {}
	for r in record:
		if r[0][0] == 'E':
			result.append([r[0], r[1]])
			rec_dic[r[1]] = r[2]
		elif r[0][0] == 'C':
			rec_dic[r[1]] = r[2]
		else:
			result.append([r[0], r[1]])
	answer = [f'{rec_dic[r[1]]}님이 {in_out[r[0]]}' for r in result]
	return answer

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])

'''
record : ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
result : ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
'''