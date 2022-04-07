from itertools import combinations
import sys

N = int(sys.stdin.readline())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# lst = list(range(N))
# combi_list = combinations(lst, N//2)
# balanced = 30*N*N
# for combi in combi_list:
# 	balance = 0
# 	other = [ k for k in range(N) if k not in combi]
# 	for i in range(N//2):
# 		for j in range(N//2):
# 			balance += S[combi[i]][combi[j]] - S[other[i]][other[j]]
# 	else:
# 		balance = abs(balance)
# 		if balance < balanced:
# 			balanced = balance
# 	if balanced == 0:
# 		break
# print(balanced)
lst = list(range(N))
sums = [0]*N
total = 0
for i in range(N):
	sums[i] += sum(S[i])
	total += sum(S[i])
	for j in range(N):
		sums[i] += S[j][i]
min_balance = 26*N*N
for cb in combinations(lst,N//2):
	tmp = 0
	for c in cb:
		tmp += sums[c]
	diff = abs(total - tmp)

	if diff < min_balance:
		min_balance = diff
print(min_balance)



# def my_comb(combi, idx):
# 	global comb_cnt, N
# 	if comb_cnt >
# 	if len(combi) == N//2:
# 		combi
# 		print(ans)
# 		comb_cnt += 1
# 		return
# 	else:
# 		for i in range(idx, len(lst)):
# 			if i not in combi:
# 				combi.add(i)
# 				my_comb(combi, i)
# 				combi.remove(i)
#my_comb(set(), 0)
#print(comb_cnt)