N = int(input())
col = [0, 1, 2, 1, 2]
if N == 4 or N == 7:
	print(-1)
else:
	print(N//5+col[N%5])
#
# if N%5 == 0:
# 	print(N//5)
# elif N%5 == 1:
# 	print(N//5+1)
# elif N%5 == 2:
# 	if N//5 >= 2:
# 		print(N//5 +2)
# 	else:
# 		print(-1)
# elif N%5 == 3:
# 	print(N//5 + 1)
# elif N%5 == 4:
# 	if N//5 >= 1:
# 		print(N//5+2)
# 	else:
# 		print(-1)