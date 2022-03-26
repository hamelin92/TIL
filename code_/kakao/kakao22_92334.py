def solution(id_list, report, k):
	id_idx = { id_list[i]: i for i in range(len(id_list))}
	#index 함수 기능 대체하기 위한 딕셔너리
	check = [[0]*len(id_list) for _ in range(len(id_list))]
	# (신고한 사람, 신고당한 사람)으로 이루어진 그래프를 나타내는 2차 리스트
	cnt_lst = [0]*len(id_list)
	# 각각의 피신고 횟수를 카운트하기 위한 리스트
	answer = [0]*len(id_list)
	#결과 ( 신고 후 받은 메일의 개수 )를 저장할 리스트
	for ids in report: #신고 목록을 순회
		info = list(ids.split())
		# 각각의 신고 건에 대해 split을 이용하여 [ 신고자id, 신고당하는 id]로 나타낸다.
		i, j =id_idx[info[0]], id_idx[info[1]]
		# 신고자와 피신고자의 인덱스를 각각 i,j로 저장.
		if check[i][j] == 0:
			# 해당 신고자가 대상을 처음 신고하는 경우 ( 같은 사람이 같은 대상을 여러번 신고하는 중복건수를 제외하기 위함)
			check[i][j] = 1 # check 리스트의 해당 좌표에 1을 저장
			cnt_lst[j] += 1 # 신고 대상의 인덱스에 대해 cnt +1
	for idx in range(len(id_list)): # 신고 완료 후 피신고 회수 체크 ( cnt 값 확인)
		if cnt_lst[idx] >= k: # k 이상인 경우만 확인
			for i in range(len(id_list)): #그 경우 check 리스트의 idx열을 확인한다.
				if check[i][idx] == 1: # 0행~끝까지 idx열을 확인해서 1인 경우 answer의 i 인덱스 값을 +1 해준다.
					answer[i] += 1
	return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
'''
["muzi", "frodo", "apeach", "neo"]	["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]	2	[2,1,1,0]
'''