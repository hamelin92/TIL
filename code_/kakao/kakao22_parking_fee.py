def solution(fees, records):
	from collections import defaultdict
	answer = []
	dic = defaultdict(list)
	for record in records:
		new_record = record.split()
		dic[new_record[1]].append([new_record[0], new_record[2]])
	order = sorted(dic, key = int)
	end = 1439
	check_in = 0
	check_out = -1
	for key in order:
		fee = 0
		minutes = 0
		for rec in dic[key]:
			if rec[1] == 'IN':
				check_in = int(rec[0][0:2]) * 60 + int(rec[0][3:])

			else:
				check_out = int(rec[0][0:2]) * 60 + int(rec[0][3:])
				minutes += check_out - check_in
		if check_in > check_out:
			minutes += end - check_in
		minutes -= fees[0]
		fee += fees[1]
		if minutes > 0:
			additional = divmod(minutes, fees[2])
			if additional[1] > 0:
				fee += (additional[0]+1) * fees[3]
			else:
				fee += additional[0] * fees[3]
		answer.append(fee)
	print(answer)
	return answer
solution([120, 0, 60, 591],["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"])
'''
[180, 5000, 10, 600]
["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
[14600, 34400, 5000]
[120, 0, 60, 591]	["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
'''
