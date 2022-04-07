def solution(orders, course): # orders
	from collections import defaultdict
	from itertools import combinations
	answer = []
	cnt_dic = defaultdict(int)
	for order in orders:
		for menu in order:
			cnt_dic[menu] += 1

	ordered_key = sorted(cnt_dic.keys(), reverse=True)
	for n in course:
		res = []
		tmp_ans = []
		max_cnt = 0
		for key in ordered_key:

			if cnt_dic[key] >= 2:
				res.append(key)
		for cb in combinations(res, n):
			comb_cnt = 0
			comb = ''
			for menu in sorted(cb):
				comb += menu
			for order in orders:
				for menu in cb:
					if menu not in order:
						break
				else:
					comb_cnt += 1
			else:
				if comb_cnt >= 2:
					if comb_cnt > max_cnt:
						max_cnt = comb_cnt
						tmp_ans.clear()
						tmp_ans.append(comb)
					elif comb_cnt == max_cnt:
						tmp_ans.append(comb)
		else:
			answer.extend(tmp_ans)
	answer.sort()
	return answer
solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4])


'''
orders	                                            course	   result
["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]	    [2,3,4]	  ["AC", "ACDE", "BCFG", "CDE"]
["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]	[2,3,5]	  ["ACD", "AD", "ADE", "CD", "XYZ"]
["XYZ", "XWY", "WXA"]	                            [2,3,4]	  ["WX", "XY"]
'''