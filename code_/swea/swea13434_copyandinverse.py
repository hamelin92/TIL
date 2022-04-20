import math
def determinant_recursive(A, total=0):
	# Section 1: store indices in list for row referencing
	indices = list(range(len(A)))

	# Section 2: when at 2x2 submatrices recursive calls end
	if len(A) == 2 and len(A[0]) == 2:
		val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
		return val

	# Section 3: define submatrix for focus column and
	#      call this function
	for fc in indices:  # A) for each focus column, ...
		# find the submatrix ...
		As = [[A[i][j] for j in range(len(A[i]))] for i in range(len(A))]  # B) make a copy, and ...
		As = As[1:]  # ... C) remove the first row
		height = len(As)  # D)

		for i in range(height):
			# E) for each remaining row of submatrix ...
			#     remove the focus column elements
			As[i] = As[i][0:fc] + As[i][fc + 1:]

		sign = (-1) ** (fc % 2)  # F)
		# G) pass submatrix recursively
		sub_det = determinant_recursive(As)
		# H) total all returns from recursion
		total += sign * A[0][fc] * sub_det

	return total
def adj_cofactor(graph):
	N = len(graph)
	adj = [[0]*(N-1) for _ in range(N-1)]
	for g in graph:
		for num in g:
			if num > 0:
				adj[num-1][num-1] += 1
		if g[0] > 0 and g[1] > 0:
			adj[g[0]-1][g[1]-1] = -1
			adj[g[1]-1][g[0]-1] = -1
	return adj
T = int(input())
for tc in range(1, T+1):
	N, M, K = map(int, input().split())
	graphs = [list(map(int, input().split())) for _ in range(M)]
	if graphs:
		C = adj_cofactor(graphs)
		d = determinant_recursive(C, total=0)
	else:
		d = 1
	if d > 0:
		result = (((N*K)**(N*K-2))//(d**K))%1000000007
	else:
		result = 0
	print(f'#{tc} {result}')

'''
4
3 0 1
3 3 2
0 1
0 2
1 2
3 3 1
0 1
0 2
2 1
30 5 100
0 1
1 2
2 3
3 4
4 0
'''