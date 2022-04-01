def solution(orders, course): # orders
	from collections import defaultdict
	from itertools import combinations
	answer = []
	cnt_dic = defaultdict(int)
	for order in orders:
		for menu in order:
			cnt_dic[menu] += 1

	ordered_key = sorted(cnt_dic,key = lambda x: x )
	for n in course:
		res = []
		for key in ordered_key:
			if cnt_dic[key] >= n:
				res.append(key)
		for cb in combinations(res, n):
			answer.append(cb)
	print(cnt_dic)
	return
solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4])


'''
orders	                                            course	   result
["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]	    [2,3,4]	  ["AC", "ACDE", "BCFG", "CDE"]
["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]	[2,3,5]	  ["ACD", "AD", "ADE", "CD", "XYZ"]
["XYZ", "XWY", "WXA"]	                            [2,3,4]	  ["WX", "XY"]
'''